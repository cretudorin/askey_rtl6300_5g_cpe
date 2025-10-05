import logging
from datetime import timedelta
import aiohttp
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .utils import AskeyUtils
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class AskeyDataUpdateCoordinator(DataUpdateCoordinator):
    """Coordinator for fetching data from the Askey API."""

    def __init__(
        self, hass: HomeAssistant, config_entry: ConfigEntry, utils: AskeyUtils
    ):
        """Initialize the coordinator."""
        self.host = config_entry.data.get("host")
        self.utils = utils
        self.base_url = f"http://{self.host}"
        self.session = aiohttp.ClientSession()
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=SCAN_INTERVAL),
        )

    async def _async_update_data(self):
        """Fetch data from the API and update state."""
        try:
            result = {
                "throughput": await self.get_throughput(),
                "status_info_v4": await self.get_status_info_v4(),
                "status_info_v6": await self.get_status_info_v6(),
                "cellular_info_ex": await self.get_cellular_info_ex(),
                "cellular_info": await self.get_cellular_info(),
                "sms_inbox_count": await self.get_inbox_count(),
                "sms_outbox_count": await self.get_outbox_count(),
                "cellular_stats": await self.get_cellular_stats(),
                "traffic_monthly": await self.get_traffic_monthly(),
            }
            _LOGGER.info(f"Fetched data: {result}")
            return result
        except Exception as err:
            _LOGGER.error(f"Error fetching data from Askey API: {err}")
            raise UpdateFailed(f"Failed to fetch data: {err}")

    # {"Status":"ok","ModuleCommand":"/lte/throughput","Result":{"up":"xxx","down":"yyy"}}
    async def get_throughput(self):
        return await self.utils.get("/lte/throughput")

    # {"Status":"ok","ModuleCommand":"/CMGR/v4_status_info","Result":{"connectivity_type":"1","protocol":"0","connect_status":"0","ifname":"interface","ip":"xxx.0.2.0","netmask":"255.255.255.0","gateway":"xxx.0.2.1","primary_dns":"xx.xx.xx.1","secondary_dns":"xx.xx.xx.2","connect_time":"XX.XX"}}
    async def get_status_info_v4(self):
        return await self.utils.get("/CMGR/v4_status_info")

    # {"Status":"ok","ModuleCommand":"/CMGR/v6_status_info","Result":{"connectivity_type":"1","protocol":"0","connect_status":"3","ifname":"interface","ip":"","plen":"0","pd_addr":"","pd_len":"0","gateway":"","primary_dns":"","secondary_dns":"","connect_time":"XX.XX"}}
    async def get_status_info_v6(self):
        return await self.utils.get("/CMGR/v6_status_info")

    # {"Status":"ok","ModuleCommand":"/lte/cellular_info_ex","Result":{"data":[{"pci":"XXX","rssi":"-XX.XX","rsrp":"-XX.XX","rsrq":"-X.XX","sinr":"XX.X","band":"X","bandw":"XX.XXXXXX","rxch":"XXX","txch":"XXXXX","rxfreq":"XXXX.XX","txfreq":"XXXX.XX"},{"pci":"XXX","rssi":"-XX.XX","rsrp":"-XX.XX","rsrq":"-X.XX","sinr":"XX.X","band":"XX","bandw":"XX.XXXXXX","rxch":"XXXX","txch":"XXXXX","rxfreq":"XXX.X","txfreq":"XXX.X"}]}}
    async def get_cellular_info_ex(self):
        return await self.utils.get("/lte/cellular_info_ex")

    # {"Status":"ok","ModuleCommand":"/lte/cellular_info","Result":{"type":"LTE","gci":"XXXXXXX","mcc":"XXX","mnc":"X","tac":"XXXXX","enb":"XXXXX","serv_time":"XXXXXX","cqi":"XX","count":"X"}}
    async def get_cellular_info(self):
        return await self.utils.get("/lte/cellular_info")

    # {"Status":"ok","ModuleCommand":"/sms/inbox_list_count","Result":{ "totalcount":"1" }}
    async def get_inbox_count(self):
        return await self.utils.get("/sms/inbox_list_count")

    # {"Status":"ok","ModuleCommand":"/sms/outbox_list_count","Result":{ "totalcount":"42" }}
    async def get_outbox_count(self):
        return await self.utils.get("/sms/outbox_list_count")

    # {"Status":"ok","ModuleCommand":"/lte/cellular_stats","Result":{"tx_bytes":"329721290","rx_bytes":"1106203912","tx_dropped":"0","rx_dropped":"0","tx_error":"0","rx_error":"0","tx_packets":"2427066","rx_packets":"2977705"}}
    async def get_cellular_stats(self):
        return await self.utils.get("/lte/cellular_stats")

    # {"Status":"ok","ModuleCommand":"/traffic/monthly","Result":{"rx":"55.34GB","tx":"18.56GB","total":"73.90GB","updated_datetime":"2025-10-09 20:09"}}
    async def get_traffic_monthly(self):
        return await self.utils.get("/traffic/monthly")

    async def async_request_data(self):
        """Manually trigger data update."""
        return await self.async_refresh()
