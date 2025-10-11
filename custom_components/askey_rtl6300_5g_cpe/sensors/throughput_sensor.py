import logging

from custom_components.askey_rtl6300_5g_cpe.utils import bytes_to_mib, safe_get_property

from .base_sensor import AskeyBaseSensorDiagnostic
from homeassistant.const import UnitOfInformation


_LOGGER = logging.getLogger(__name__)


class AskeyThroughputDownloadSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the allocated download bandwidth.
    Represents the current allocated bandwidth for download, not the actual throughput.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Allocated Bandwidth Download",
            "askey_reserved_down",
            "mdi:download-network",
            "down",
            UnitOfInformation.MEBIBYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["throughput", "down"],
            bytes_to_mib,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Shows the allocated download bandwidth (not the actual throughput).",
            "Unit": UnitOfInformation.MEBIBYTES,
        }


class AskeyThroughputUploadSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the allocated upload bandwidth.
    Represents the current allocated bandwidth for upload, not the actual throughput.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Allocated Bandwidth Upload",
            "askey_reserved_up",
            "mdi:upload-network",
            "up",
            UnitOfInformation.MEBIBYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["throughput", "up"],
            bytes_to_mib,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Shows the allocated upload bandwidth (not the actual throughput).",
            "Unit": UnitOfInformation.MEBIBYTES,
        }
