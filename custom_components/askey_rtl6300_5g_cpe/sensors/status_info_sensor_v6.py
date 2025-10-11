from ..utils import map_connect_status, safe_get_property
from .base_sensor import AskeyBaseSensor
from .base_sensor import AskeyBaseSensorDiagnostic


class AskeyConnectivityStatusSensorV6(AskeyBaseSensor):
    """
    Sensor for monitoring the IPv6 connectivity status.
    Provides the status of the IPv6 connection based on connectivity status.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv6 Status",
            "askey_status_v6",
            "mdi:network",
            "connect_status",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        status = "Disabled"  # Default status if not found

        if data and "status_info_v6" in data:
            statusInfoV6 = data["status_info_v6"]

            # If statusInfoV6 is a list, iterate over it
            if isinstance(statusInfoV6, list):
                for item in statusInfoV6:
                    if item.get("connectivity_type") == "1":
                        status = map_connect_status(item.get("connect_status"))
                        break
            else:
                # Fallback: If statusInfoV6 is a single object
                if statusInfoV6.get("connectivity_type") == "1":
                    status = map_connect_status(statusInfoV6.get("connect_status"))

        return status

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the current IPv6 connectivity status.",
            "Unit": "None",
        }


class AskeyConnectivityIpSensorV6(AskeyBaseSensor):
    """
    Sensor for monitoring the external IPv6 address.
    Provides the external IP address assigned to the device.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "External IPv6",
            "askey_ip_v6",
            "mdi:network",
            "ip",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["status_info_v6", "ip"])

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the external IPv6 address of the device.",
            "Unit": "None",
        }


class AskeyConnectivityGatewaySensorV6(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the IPv6 gateway address.
    Provides the IP address of the gateway used for routing the traffic.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv6 Gateway",
            "askey_v6_gateway",
            "mdi:router-network",
            "",
        )

    @property
    def native_value(self):
        return safe_get_property(self.coordinator.data, ["status_info_v6", "gateway"])

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IPv6 gateway address used for routing.",
            "Unit": "None",
        }


class AskeyConnectivityPrimaryDNSSensorV6(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Primary DNS IPv6 address.
    Provides the IP address of the primary DNS server used for name resolution.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv6 DNS 1",
            "askey_v6_dns1",
            "mdi:dns",
            "primary_dns",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["status_info_v6", "primary_dns"]
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IP address of the primary DNS server for IPv6.",
            "Unit": "None",
        }


class AskeyConnectivitySecondaryDNSSensorV6(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Secondary DNS IPv6 address.
    Provides the IP address of the secondary DNS server used for name resolution.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv6 DNS 2",
            "askey_v6_dns2",
            "mdi:dns",
            "secondary_dns",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["status_info_v6", "secondary_dns"]
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IP address of the secondary DNS server for IPv6.",
            "Unit": "None",
        }
