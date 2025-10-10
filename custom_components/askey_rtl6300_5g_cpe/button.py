from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import AskeyDataUpdateCoordinator
from .utils import AskeyUtils
from .coordinator import AskeyDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up the ASKEY button platform."""
    utils = AskeyUtils(hass, entry)
    coordinator = AskeyDataUpdateCoordinator(hass, entry, utils)

    async_add_entities(
        [
            AskeyBaseButton(
                coordinator=coordinator,
                name="Restart Router",
                unique_id="askey_restart_button",
                icon="mdi:restart",
                press_action=coordinator.handle_restart,
            ),
            AskeyBaseButton(
                coordinator=coordinator,
                name="Reconnect",
                unique_id="askey_reconnect_button",
                icon="mdi:connection",
                press_action=coordinator.handle_reconnect,
            ),
        ],
    )


class AskeyBaseButton(ButtonEntity):
    """Base class for ASKEY buttons."""

    def __init__(self, coordinator, name, unique_id, icon, press_action):
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_icon = icon
        self._press_action = press_action
        self._attr_has_entity_name = True

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "askey_router")},
            "name": "ASKEY 5G Router",
            "manufacturer": "ASKEY",
            "model": "5G Home Router",
        }

    async def async_press(self):
        await self._press_action()
        await self.coordinator.async_request_refresh()
