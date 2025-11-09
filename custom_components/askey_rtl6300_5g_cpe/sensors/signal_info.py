from custom_components.askey_rtl6300_5g_cpe.utils import safe_get_property
from .base_sensor import AskeyBaseSensorDiagnostic


class Askey5gRsrpSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G Reference Signal Received Power (RSRP)."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "5G RSRP", "askey_5g_rsrp", "mdi:signal", "5g_rsrp", "dBm"
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_rsrp"])

    @property
    def extra_state_attributes(self):
        return {
            "Description": "5G Reference Signal Received Power (RSRP) in dBm.",
            "Unit": "dBm",
        }


class Askey5gRsrqSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G Reference Signal Received Quality (RSRQ)."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "5G RSRQ", "askey_5g_rsrq", "mdi:signal", "5g_rsrq", "dB"
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_rsrq"])

    @property
    def extra_state_attributes(self):
        return {
            "Description": "5G Reference Signal Received Quality (RSRQ) in dB.",
            "Unit": "dB",
        }


class Askey5gSinrSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G Signal-to-Interference-plus-Noise Ratio (SINR)."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "5G SINR", "askey_5g_sinr", "mdi:signal", "5g_sinr"
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_sinr"])

    @property
    def extra_state_attributes(self):
        return {
            "Description": "5G Signal-to-Interference-plus-Noise Ratio (SINR) in dB.",
            "Unit": "dB",
        }


class Askey5gPciSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G Physical Cell ID (PCI)."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "5G PCI", "askey_5g_pci", "mdi:signal", "5g_pci")

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_pci"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G Physical Cell Identity (PCI).", "Unit": "None"}


class Askey5gBandSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G frequency band."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "5G Band", "askey_5g_band", "mdi:signal", "5g_band"
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_band"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G frequency band number.", "Unit": "None"}


class Askey5gBandwidthSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G channel bandwidth."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G Bandwidth",
            "askey_5g_bandwidth",
            "mdi:network",
            "5g_bandw",
            "MHz",
        )

    @property
    def extra_state_attributes(self):
        return {"Description": "5G channel bandwidth", "Unit": "MHz"}

    @property
    def native_value(self):
        try:
            return float(
                safe_get_property(self.coordinator.data, ["signal_info", "5g_bandw"])
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None


class Askey5gTxPowerSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G transmit power."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G TX Power",
            "askey_5g_txpwr",
            "mdi:transmission-tower",
            "5g_txpwr",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_txpwr"])

    @property
    def extra_state_attributes(self):
        return {
            "Description": "5G transmit power in dBm (if available).",
            "Unit": "dBm",
        }


class Askey5gRxChannelSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G downlink channel (DL ARFCN)."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G RX Channel",
            "askey_5g_rxch",
            "mdi:signal",
            "5g_rxch",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_rxch"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G downlink channel number (ARFCN).", "Unit": "None"}


class Askey5gTxChannelSensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G uplink channel (UL ARFCN)."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G TX Channel",
            "askey_5g_txch",
            "mdi:signal",
            "5g_txch",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "5g_txch"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G uplink channel number (ARFCN).", "Unit": "None"}


class Askey5gRxFrequencySensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G downlink frequency."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G RX Frequency",
            "askey_5g_rxfreq",
            "mdi:signal",
            "nr5g_rxfreq",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "nr5g_rxfreq"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G downlink frequency in MHz.", "Unit": "MHz"}


class Askey5gTxFrequencySensor(AskeyBaseSensorDiagnostic):
    """Sensor for monitoring the 5G uplink frequency."""

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "5G TX Frequency",
            "askey_5g_txfreq",
            "mdi:signal",
            "nr5g_txfreq",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["signal_info", "nr5g_txfreq"])

    @property
    def extra_state_attributes(self):
        return {"Description": "5G uplink frequency in MHz.", "Unit": "MHz"}
