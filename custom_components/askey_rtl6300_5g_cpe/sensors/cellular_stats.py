from .base_sensor import AskeyBaseSensor, AskeyBaseSensorDiagnostic
from homeassistant.const import UnitOfInformation


class AskeyTxBytesSensor(AskeyBaseSensor):
    """
    Tracks the amount of data transmitted (TX) since the last restart.
    Data is received in bytes and converted to GiB.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Current Upload",
            "askey_tx",
            "mdi:upload",
            "tx_bytes",
            UnitOfInformation.GIBIBYTES,
        )

    @property
    def native_value(self):
        try:
            if self.coordinator.data:
                raw = self.coordinator.data.get("cellular_stats", {}).get("tx_bytes")
                if raw is None:
                    return 0
                mib = int(raw) / 1_048_576
                return round(mib / 1024, 2)
            return 0
        except (TypeError, ValueError):
            return 0

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the amount of data transmitted (TX) since the last restart.",
            "Unit": "GiB",
        }


class AskeyRxBytesSensor(AskeyBaseSensor):
    """
    Tracks the amount of data received (RX) since the last restart.
    Data is received in bytes and converted to MiB.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Current Download",
            "askey_rx",
            "mdi:download",
            "rx_bytes",
            UnitOfInformation.GIBIBYTES,
        )

    @property
    def native_value(self):
        try:
            if self.coordinator.data:
                raw = self.coordinator.data.get("cellular_stats", {}).get("rx_bytes")
                if raw is None:
                    return 0
                mib = int(raw) / 1_048_576
                return round(mib / 1024, 2)
            return 0
        except (TypeError, ValueError):
            return 0

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the amount of data received (RX) since the last restart.",
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
            "mdi:packet",
            "tx_dropped",
        )

    @property
    def native_value(self):
        try:
            if self.coordinator.data:
                value = self.coordinator.data.get("cellular_stats", {}).get(
                    "tx_dropped"
                )
                return int(value) if value is not None and value.isdigit() else 0
            return 0
        except (TypeError, ValueError):
            return 0

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
            "mdi:packet",
            "rx_dropped",
        )

    @property
    def native_value(self):
        try:
            if self.coordinator.data:
                value = self.coordinator.data.get("cellular_stats", {}).get(
                    "rx_dropped"
                )
                return int(value) if value is not None and value.isdigit() else 0
            return 0
        except (TypeError, ValueError):
            return 0

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
        try:
            if self.coordinator.data:
                return int(
                    self.coordinator.data.get("cellular_stats", {}).get("tx_error")
                )
            return None
        except (TypeError, ValueError):
            return None

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
        try:
            if self.coordinator.data:
                value = self.coordinator.data.get("cellular_stats", {}).get("rx_error")
                return int(value) if value is not None and value.isdigit() else 0
            return 0
        except (TypeError, ValueError):
            return 0

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
        try:
            if self.coordinator.data:
                value = self.coordinator.data.get("cellular_stats", {}).get(
                    "tx_packets"
                )
                return int(value) if value is not None and value.isdigit() else 0
            return 0
        except (TypeError, ValueError):
            return 0

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
        try:
            if self.coordinator.data:
                value = self.coordinator.data.get("cellular_stats", {}).get(
                    "rx_packets"
                )
                return int(value) if value is not None and value.isdigit() else 0
            return 0
        except (TypeError, ValueError):
            return 0

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Tracks the number of received packets (RX) successfully received from the network since the last restart.",
        }
