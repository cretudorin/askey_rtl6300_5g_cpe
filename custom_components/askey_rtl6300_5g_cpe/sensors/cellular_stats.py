from custom_components.askey_rtl6300_5g_cpe.utils import (
    bytes_to_gib,
    safe_get_property,
)
from .base_sensor import AskeyBaseSensor, AskeyBaseSensorDiagnostic
from homeassistant.const import UnitOfInformation


class AskeyTxBytesSensor(AskeyBaseSensor):
    """
    Tracks the amount of data sent in last 24 hours(ish).
    Data is sent in bytes and converted to GiB.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Current Upload",
            "askey_upload",
            "mdi:upload",
            "upload",
            UnitOfInformation.GIBIBYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["cellular_stats", "tx_bytes"],
            bytes_to_gib,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the amount of data transmitted in the current session, resets everyday",
            "Unit": "GiB",
        }


class AskeyRxBytesSensor(AskeyBaseSensor):
    """
    Tracks the amount of data received in last 24 hours(ish).
    Data is received in bytes and converted to GiB.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Current Download",
            "askey_download",
            "mdi:download",
            "download",
            UnitOfInformation.GIBIBYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["cellular_stats", "rx_bytes"],
            bytes_to_gib,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the amount of data received in the current session, resets everyday",
            "Unit": "GiB",
        }


class AskeyTxDroppedSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of dropped transmitted packets (TX Dropped) on the network.
    Represents the number of packets dropped during transmission since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "TX Dropped",
            "askey_tx_dropped",
            "mdi:alert-circle",
            "tx_dropped",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "tx_dropped"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of transmitted packets (TX) dropped during transmission since the last restart.",
        }


class AskeyRxDroppedSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of dropped received packets (RX Dropped) on the network.
    Represents the number of packets dropped during reception since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "RX Dropped",
            "askey_rx_dropped",
            "mdi:alert-circle",
            "rx_dropped",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "rx_dropped"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of received packets (RX) dropped during reception since the last restart.",
        }


class AskeyTxErrorSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of transmitted packets errors (TX Errors).
    Represents the number of errors encountered during transmission since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "TX Errors",
            "askey_tx_errors",
            "mdi:alert-circle",
            "tx_error",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "tx_error"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of transmitted packets (TX) errors encountered during transmission since the last restart.",
        }


class AskeyRxErrorSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of received packets errors (RX Errors).
    Represents the number of errors encountered during reception since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "RX Errors",
            "askey_rx_errors",
            "mdi:alert-circle",
            "rx_error",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "rx_error"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of received packets (RX) errors encountered during reception since the last restart.",
        }


class AskeyTxPacketsSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of transmitted packets (TX Packets).
    Represents the number of packets successfully transmitted on the network since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "TX Packets",
            "askey_tx_packets",
            "mdi:packet",
            "tx_packets",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "tx_packets"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of transmitted packets (TX) successfully transmitted on the network since the last restart.",
        }


class AskeyRxPacketsSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the number of received packets (RX Packets).
    Represents the number of packets successfully received from the network since the last restart.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "RX Packets",
            "askey_rx_packets",
            "mdi:packet",
            "rx_packets",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["cellular_stats", "rx_packets"], int
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of received packets (RX) successfully received from the network since the last restart.",
        }
