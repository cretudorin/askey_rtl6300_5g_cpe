from .base_sensor import AskeyBaseSensorDiagnostic

"""
SCC1 is not always present and the router has changes the json respose structure in that case.
not worth using safe_get_property
"""


class AskeyScc1PciSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Physical Cell Identity (PCI) of SCC1.
    PCI is used to identify the specific cell within a network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "SCC1 PCI", "askey_scc1_pci", "mdi:network", "pci"
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][1]["pci"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Physical Cell Identity (PCI) of SCC1 used to identify cells within the network.",
            "Unit": "None",
        }


class AskeyScc1RssiSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Received Signal Strength Indicator (RSSI) of SCC1.
    RSSI measures the power level of the received signal, indicating signal strength.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 RSSI",
            "askey_scc1_rssi",
            "mdi:signal",
            "rssi",
            "dBm",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["rssi"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Received Signal Strength Indicator (RSSI) of SCC1. A measure of the power level being received by the device.",
            "Unit": "dBm",
        }


class AskeyScc1RsrpSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Power (RSRP) of SCC1.
    RSRP indicates the strength of the reference signal, which is important for connection stability.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 RSRP",
            "askey_scc1_rsrp",
            "mdi:signal",
            "rsrp",
            "dBm",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["rsrp"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Power (RSRP) of SCC1. Indicates the strength of the reference signal.",
            "Unit": "dBm",
        }


class AskeyScc1RsrqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Quality (RSRQ) of SCC1.
    RSRQ is a measure of signal quality, combining signal strength and interference.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 RSRQ",
            "askey_scc1_rsrq",
            "mdi:signal",
            "rsrq",
            "dB",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["rsrq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Quality (RSRQ) of SCC1. A measure of signal quality combining signal strength and interference.",
            "Unit": "dB",
        }


class AskeyScc1SinrSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Signal to Interference plus Noise Ratio (SINR) of SCC1.
    SINR measures the quality of the received signal relative to interference and noise.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 SINR",
            "askey_scc1_sinr",
            "mdi:signal",
            "sinr",
            "dB",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["sinr"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Signal to Interference plus Noise Ratio (SINR) of SCC1. Measures the quality of the signal relative to interference and noise.",
            "Unit": "dB",
        }


class AskeyScc1BandSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the cellular frequency band of SCC1.
    The band determines the frequency range for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "SCC1 Band", "askey_scc1_band", "mdi:network", "band"
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][1]["band"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Cellular frequency band of SCC1.", "Unit": "None"}


class AskeyScc1BandwSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the bandwidth (in MHz) of SCC1.
    The bandwidth indicates the width of the frequency band used for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 Bandwidth",
            "askey_scc1_bandw",
            "mdi:network",
            "bandw",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["bandw"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Bandwidth of SCC1 in megahertz (MHz).", "Unit": "MHz"}


class AskeyScc1RxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive channel (RX) of SCC1.
    This channel is used for receiving data in the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 RX Channel",
            "askey_scc1_rxch",
            "mdi:radio-tower",
            "rxch",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][1]["rxch"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Receive Channel for SCC1.", "Unit": "None"}


class AskeyScc1TxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit channel (TX) of SCC1.
    This channel is used for sending data to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 TX Channel",
            "askey_scc1_txch",
            "mdi:radio-tower",
            "txch",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][1]["txch"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Transmit Channel for SCC1.", "Unit": "None"}


class AskeyScc1RxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive frequency (RX) of SCC1 in megahertz (MHz).
    This frequency is used for receiving signals from the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 RX Freq",
            "askey_scc1_rxfreq",
            "mdi:radio-tower",
            "rxfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["rxfreq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Receive Frequency for SCC1 in megahertz (MHz).",
            "Unit": "MHz",
        }


class AskeyScc1TxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit frequency (TX) of SCC1 in megahertz (MHz).
    This frequency is used for transmitting signals to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC1 TX Freq",
            "askey_scc1_txfreq",
            "mdi:radio-tower",
            "txfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][1]["txfreq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Transmit Frequency for SCC1 in megahertz (MHz).",
            "Unit": "MHz",
        }
