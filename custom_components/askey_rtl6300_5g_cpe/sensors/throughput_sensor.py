import logging

from .base_sensor import AskeyBaseSensorDiagnostic
from ..const import DOMAIN
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
        data = self.coordinator.data
        if data and "throughput" in data:
            download_bps = data["throughput"].get("down")
            if download_bps is not None:
                try:
                    return round(float(download_bps) / 1_048_576, 2)
                except ValueError:
                    _LOGGER.error(
                        f"Invalid download throughput value: %s", download_bps
                    )
        return None

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
        data = self.coordinator.data
        if data and "throughput" in data:
            upload_bps = data["throughput"].get("up")
            if upload_bps is not None:
                try:
                    return round(float(upload_bps) / 1_048_576, 2)
                except ValueError:
                    _LOGGER.error(f"Invalid upload throughput value: %s", upload_bps)
        return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Shows the allocated upload bandwidth (not the actual throughput).",
            "Unit": UnitOfInformation.MEBIBYTES,
        }
