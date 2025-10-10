from .base_sensor import AskeyBaseSensorDiagnostic, AskeyBaseSensor
from datetime import timedelta
from homeassistant.const import UnitOfTime


class AskeyPccTypeSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the network type (e.g., LTE).
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Connection Type",
            "askey_pcc_type",
            "mdi:network",
            "type",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["type"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Network type (LTE or 5G)", "Unit": "None"}


class AskeyPccGciSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Global Cell Identity (GCI).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC GCI", "askey_pcc_gci", "mdi:network", "gci")

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["gci"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Global Cell Identity (GCI).", "Unit": "None"}


class AskeyPccMccSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Mobile Country Code (MCC).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC MCC", "askey_pcc_mcc", "mdi:network", "mcc")

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["mcc"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Mobile Country Code (MCC).", "Unit": "None"}


class AskeyPccMncSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Mobile Network Code (MNC).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC MNC", "askey_pcc_mnc", "mdi:network", "mnc")

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["mnc"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Mobile Network Code (MNC).", "Unit": "None"}


class AskeyPccTacSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Tracking Area Code (TAC).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC TAC", "askey_pcc_tac", "mdi:network", "tac")

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["tac"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Tracking Area Code (TAC).", "Unit": "None"}


class AskeyPccEnbSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the eNodeB ID (ENB).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC ENB", "askey_pcc_enb", "mdi:network", "enb")

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["enb"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "eNodeB ID (ENB).", "Unit": "None"}


class AskeyPccServTimeSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the serving time.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "PCC Serving Time",
            "askey_pcc_serv_time",
            "mdi:clock",
            "serv_time",
            UnitOfTime.SECONDS,
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info"]["serv_time"]
        except (KeyError, TypeError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        try:
            serv_time_seconds = int(self.coordinator.data["cellular_info"]["serv_time"])
            serv_time_str = str(timedelta(seconds=serv_time_seconds))
            return {
                "Description": "Serving time in HH:MM:SS format.",
                "Unit": "HH:MM:SS",
                "time": serv_time_str,
            }
        except (KeyError, TypeError, ValueError):
            return {
                "Description": "Serving time in HH:MM:SS format.",
                "Unit": "HH:MM:SS",
                "time": None,
            }


class AskeyPccCqiSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Channel Quality Indicator (CQI).
    """

    def __init__(self, coordinator):
        super().__init__(coordinator, "PCC CQI", "askey_pcc_cqi", "mdi:signal", "cqi")

    @property
    def native_value(self):
        try:
            return int(self.coordinator.data["cellular_info"]["cqi"])
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Channel Quality Indicator (CQI).", "Unit": "None"}


class AskeyPccCountSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the count of connected cells or measurements.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "PCC Count", "askey_pcc_count", "mdi:counter", "count"
        )

    @property
    def native_value(self):
        try:
            return int(self.coordinator.data["cellular_info"]["count"])
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Count of connected cells or measurements.",
            "Unit": "None",
        }
