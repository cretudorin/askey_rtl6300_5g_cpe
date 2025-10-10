from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

import logging

from .utils import AskeyUtils

from .const import DOMAIN
from .coordinator import AskeyDataUpdateCoordinator


_LOGGER = logging.getLogger(__name__)

# import debugpy

# _LOGGER.warning("Starting debugpy listener on port 5678...")
# debugpy.listen(5678)
# _LOGGER.warning("Waiting for debugger to attach...")
# debugpy.wait_for_client()
# _LOGGER.warning("Debugger attached, continuing execution...")


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration via YAML (optional)."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the integration via UI config entry."""
    hass.data.setdefault(DOMAIN, {})
    utils = AskeyUtils(hass, entry)
    coordinator = AskeyDataUpdateCoordinator(hass, entry, utils)
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Set up platforms (e.g. sensor)
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    # Register the services using lambda functions
    hass.services.async_register(
        domain=DOMAIN,
        service="send_sms",
        service_func=utils.handle_send_sms,
    )

    hass.services.async_register(
        domain=DOMAIN,
        service="get_inbox",
        service_func=utils.handle_get_inbox,
    )

    hass.services.async_register(
        domain=DOMAIN,
        service="clear_inbox",
        service_func=utils.handle_clear_inbox,
    )

    hass.services.async_register(
        domain=DOMAIN,
        service="clear_outbox",
        service_func=utils.handle_clear_outbox,
    )

    # Forward the setup to the button platform
    await hass.config_entries.async_forward_entry_setups(entry, ["button"])

    return True
