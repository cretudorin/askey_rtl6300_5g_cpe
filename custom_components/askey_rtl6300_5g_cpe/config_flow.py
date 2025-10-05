import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, CONF_HOST, DEFAULT_HOST

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_HOST, default=DEFAULT_HOST): str,
    }
)


class AskeyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ASKEY RTL6300 5G CPE."""

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Optionally: Validate if the host is reachable
            return self.async_create_entry(title=user_input[CONF_HOST], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )
