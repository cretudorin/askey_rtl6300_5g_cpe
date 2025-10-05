from homeassistant.components.sensor import SensorEntity
from ..const import DOMAIN
from homeassistant.helpers.entity import EntityCategory


class AskeyBaseSensor(SensorEntity):
    """Base class for ASKEY sensors."""

    def __init__(self, coordinator, name, unique_id, icon, value_key, unit=None):
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_icon = icon
        self._attr_native_unit_of_measurement = unit
        self.value_key = value_key
        self._attr_has_entity_name = True

    @property
    def device_info(self):
        """Return device info to group all sensors under one device."""
        return {
            "identifiers": {(DOMAIN, "askey_router")},
            "name": "ASKEY 5G Router",
            "manufacturer": "ASKEY",
            "model": "5G Home Router",
        }

    async def async_update(self):
        """Request data refresh from coordinator."""
        await self.coordinator.async_request_refresh()


class AskeyBaseSensorDiagnostic(AskeyBaseSensor):
    """Base class for ASKEY sensors."""

    def __init__(self, coordinator, name, unique_id, icon, value_key, unit=None):
        super().__init__(coordinator, name, unique_id, icon, value_key, unit)
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
