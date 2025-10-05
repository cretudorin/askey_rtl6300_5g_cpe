import aiohttp
import json
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import CONF_HOST, DEFAULT_HOST
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall


_LOGGER = logging.getLogger(__name__)


def map_connect_status(connect_status: str):
    """Map connect_status to a human-readable value."""
    status_map = {
        "0": "Connected",
        "1": "Connecting",
        "2": "Connect Fail",
        "3": "Disconnected",
    }
    return status_map.get(connect_status, "Unknown")


class AskeyUtils:
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry):
        self.hass = hass
        self.host = config_entry.data.get(CONF_HOST, DEFAULT_HOST)
        self.base_url = f"http://{self.host}"

    async def get(self, endpoint: str):
        return await self.request("GET", endpoint)

    async def put(
        self,
        endpoint: str,
        data: dict = None,
        params: dict = None,
        headers: dict = None,
    ):
        return await self.request("PUT", endpoint, data, params, headers)

    async def request(
        self,
        method: str,
        endpoint: str,
        data: dict = None,
        params: dict = None,
        headers: dict = {"Content-Type": "application/json"},
        expected_status: int = 200,
    ) -> dict:
        """
        Generic HTTP request handler for the Askey API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., "restful/sms/inbox_list")
            data: Dictionary of data to send in the request body
            params: Dictionary of query parameters
            headers: Dictionary of headers to include
            expected_status: Expected HTTP status code (default: 200)

        Returns:
            dict: Parsed JSON response or None if request fails
        """

        url = f"{self.base_url.rstrip('/')}/restful/{endpoint.lstrip('/')}"
        session = async_get_clientsession(self.hass)

        try:
            async with session.request(
                method=method.upper(),
                url=url,
                json=data,
                params=params,
                headers=headers,
            ) as response:
                # Check if status matches expected
                if response.status != expected_status:
                    _LOGGER.error(
                        f"Unexpected status {response.status} for {method} {endpoint}. "
                        f"Expected: {expected_status}"
                    )
                    return None

                # Try to parse JSON response
                try:
                    json_response = await response.json()

                    # Validate response structure if needed
                    if json_response.get("Status") != "ok":
                        _LOGGER.warning(
                            f"API returned non-ok status for {method} {endpoint}: "
                            f"{json_response.get('Status', 'Unknown')}"
                        )
                        return None

                    return json_response.get("Result", json_response)

                except ValueError:
                    _LOGGER.error(f"Invalid JSON response from {method} {endpoint}")
                    return None

        except aiohttp.ClientError as e:
            _LOGGER.error(f"HTTP error for {method} {endpoint}: {str(e)}")
        except Exception as e:
            _LOGGER.error(f"Unexpected error for {method} {endpoint}: {str(e)}")
        return None

    async def handle_send_sms(self, call: ServiceCall):
        phone_number = call.data.get("phone_number")
        message = call.data.get("message")
        if not phone_number or not message:
            _LOGGER.error("Phone number and message are required.")
            return

        encoded_phone = phone_number.replace("+", "%2B")
        body = {"tagid": "", "phone_nums": encoded_phone, "message": message}

        try:
            result = await self.put(
                "sms/send_msg", data=body, headers={"Content-Type": "application/json"}
            )

            if result:
                _LOGGER.info(f"SMS sent successfully to {phone_number}")
                self.hass.bus.fire(
                    "askey_sms_sent",
                    {
                        "phone_number": phone_number,
                        "status": "success",
                        "response": result,
                    },
                )
                return result
            else:
                _LOGGER.error(f"Failed to send SMS to {phone_number}")
                self.hass.bus.fire(
                    "askey_sms_sent",
                    {
                        "phone_number": phone_number,
                        "status": "failed",
                        "error": "Failed to send SMS",
                    },
                )
                return None

        except Exception as e:
            _LOGGER.error(f"Error sending SMS to {phone_number}: {e}")
            self.hass.bus.fire(
                "askey_sms_sent",
                {"phone_number": phone_number, "status": "failed", "error": str(e)},
            )
            return None

    async def handle_get_inbox(self, call: ServiceCall):
        """Handle the get_inbox service call."""
        inbox_data = await self.get("/sms/inbox_list")
        if inbox_data:
            self.hass.bus.fire(
                "askey_rtl6300_5g_cpe_sms_inbox_data", {"messages": inbox_data}
            )
        return inbox_data

    async def handle_clear_inbox(self, _call: ServiceCall):
        """Handle the clear_inbox service call."""
        return await self.put(
            "sms/send_msg", json.dumps({"box": "1", "action": "1", "tagid": "all"})
        )

    async def handle_clear_outbox(self, _call: ServiceCall):
        """Handle the clear_outbox service call."""
        return await self.put(
            "sms/send_msg", json.dumps({"box": "2", "action": "1", "tagid": "all"})
        )
