from datetime import timedelta
from custom_components.askey_rtl6300_5g_cpe.utils import (
    safe_get_property,
)
from .base_sensor import AskeyBaseSensorDiagnostic, AskeyBaseSensor


class AskeyNetworkNameSensor(AskeyBaseSensor):
    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Network Name",
            "askey_network_name",
            "mdi:network",
            "network_name",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["status_info", "network_name"])

    @property
    def extra_state_attributes(self):
        return {"Description": "Network Name", "Unit": "None"}


class AskeySignalLevelSensor(AskeyBaseSensor):
    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Signal level",
            "askey_signal_level",
            "mdi:wifi",
            "signal_level",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["status_info", "signal_level"])

    @property
    def extra_state_attributes(self):
        return {"Description": "Signal level (0-5)", "Unit": "None"}


class AskeyRoamingSensor(AskeyBaseSensorDiagnostic):
    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Roaming",
            "askey_roaming",
            "mdi:signal-variant",
            "type",
        )

    @property
    def native_value(self):
        return "1" == safe_get_property(
            self.coordinator.data, ["status_info", "roam_status"]
        )

    @property
    def extra_state_attributes(self):
        return {"Description": "Signal level (0-5)", "Unit": "None"}
