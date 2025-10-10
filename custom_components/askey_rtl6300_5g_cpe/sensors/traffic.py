from homeassistant.const import UnitOfInformation
from .base_sensor import AskeyBaseSensor


class AskeyMonthlyRxSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the monthly received traffic (RX).
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Download",
            "askey_monthly_rx",
            "mdi:download",
            "rx",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        try:
            rx_str = self.coordinator.data["traffic_monthly"]["rx"]
            return float(rx_str.replace("GB", ""))
        except (KeyError, TypeError, ValueError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Monthly received traffic.",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyTxSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the monthly transmitted traffic (TX).
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Upload",
            "askey_monthly_tx",
            "mdi:upload",
            "tx",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        try:
            tx_str = self.coordinator.data["traffic_monthly"]["tx"]
            return float(tx_str.replace("GB", ""))
        except (KeyError, TypeError, ValueError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Monthly transmitted traffic.",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyTotalSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the total monthly traffic.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Total",
            "askey_monthly_total",
            "mdi:swap-horizontal",
            "total",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        try:
            total_str = self.coordinator.data["traffic_monthly"]["total"]
            return float(total_str.replace("GB", ""))
        except (KeyError, TypeError, ValueError, AttributeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Total monthly traffic",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyUpdatedDatetimeSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the last update datetime of monthly traffic data.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Last Traffic Update",
            "askey_monthly_updated_datetime",
            "mdi:calendar-clock",
            "updated_datetime",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["traffic_monthly"]["updated_datetime"]
        except (KeyError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Last update datetime of monthly traffic data.",
            "Unit": "None",
        }
