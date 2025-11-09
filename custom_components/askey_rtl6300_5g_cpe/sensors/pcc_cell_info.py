from .base_sensor import AskeyBaseSensorDiagnostic
from ..utils import get_cellular_info_ex


class AskeyPccPciSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Physical Cell Identity (PCI) of PCC.
    PCI is used to identify the specific cell within a network.
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC PCI", "askey_pcc_pci", "mdi:network", "pci")

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["pci"]
            )
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Physical Cell Identity (PCI) of PCC used to identify cells within the network.",
            "Unit": "None",
        }


class AskeyPccRssiSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Received Signal Strength Indicator (RSSI) of PCC.
    RSSI measures the power level of the received signal, indicating signal strength.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC RSSI", "askey_pcc_rssi", "mdi:signal", "rssi", "dBm"
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["rssi"]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Received Signal Strength Indicator (RSSI) of PCC. A measure of the power level being received by the device.",
            "Unit": "dBm",
        }


class AskeyPccRsrpSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Power (RSRP) of PCC.
    RSRP indicates the strength of the reference signal, which is important for connection stability.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC RSRP", "askey_pcc_rsrp", "mdi:signal", "rsrp", "dBm"
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["rsrp"]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Power (RSRP) of PCC. Indicates the strength of the reference signal.",
            "Unit": "dBm",
        }


class AskeyPccRsrqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Quality (RSRQ) of PCC.
    RSRQ is a measure of signal quality, combining signal strength and interference.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC RSRQ", "askey_pcc_rsrq", "mdi:signal", "rsrq", "dB"
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["rsrq"]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Quality (RSRQ) of PCC. A measure of signal quality combining signal strength and interference.",
            "Unit": "dB",
        }


class AskeyPccSinrSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Signal to Interference plus Noise Ratio (SINR) of PCC.
    SINR measures the quality of the received signal relative to interference and noise.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC SINR", "askey_pcc_sinr", "mdi:signal", "sinr", "dB"
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["sinr"]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Signal to Interference plus Noise Ratio (SINR) of PCC. Measures the quality of the signal relative to interference and noise.",
            "Unit": "dB",
        }


class AskeyPccBandSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the cellular frequency band of PCC.
    The band determines the frequency range for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC Band", "askey_pcc_band", "mdi:network", "band"
        )

    @property
    def native_value(self):
        try:
            get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["band"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Cellular frequency band of PCC.", "Unit": "None"}


class AskeyPccBandwSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the bandwidth (in MHz) of PCC.
    The bandwidth indicates the width of the frequency band used for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC Bandwidth",
            "askey_pcc_bandw",
            "mdi:network",
            "bandw",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["bandw"]
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Bandwidth of PCC in megahertz (MHz).", "Unit": "MHz"}


class AskeyPccRxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive channel (RX) of PCC.
    This channel is used for receiving data in the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC RX Channel",
            "askey_pcc_rxch",
            "mdi:radio-tower",
            "rxch",
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["rxch"]
            )
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Receive Channel for PCC.", "Unit": "None"}


class AskeyPccTxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit channel (TX) of PCC.
    This channel is used for sending data to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC TX Channel",
            "askey_pcc_txch",
            "mdi:radio-tower",
            "txch",
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])["txch"]
            )
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Transmit Channel for PCC.", "Unit": "None"}


class AskeyPccRxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive frequency (RX) of PCC in megahertz (MHz).
    This frequency is used for receiving signals from the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC RX Freq",
            "askey_pcc_rxfreq",
            "mdi:radio-tower",
            "rxfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])[
                    "rxfreq"
                ]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Receive Frequency for PCC in megahertz (MHz).",
            "Unit": "MHz",
        }


class AskeyPccTxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit frequency (TX) of PCC in megahertz (MHz).
    This frequency is used for transmitting signals to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC TX Freq",
            "askey_pcc_txfreq",
            "mdi:radio-tower",
            "txfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(
                get_cellular_info_ex(self.coordinator.data["cellular_info_ex"])[
                    "txfreq"
                ]
            )
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Transmit Frequency for PCC in megahertz (MHz).",
            "Unit": "MHz",
        }
