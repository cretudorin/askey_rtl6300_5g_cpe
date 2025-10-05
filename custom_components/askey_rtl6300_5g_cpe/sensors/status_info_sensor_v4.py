from ..utils import map_connect_status
from .base_sensor import AskeyBaseSensor
from .base_sensor import AskeyBaseSensorDiagnostic


class AskeyConnectivityStatusSensorV4(AskeyBaseSensor):
    """
    Sensor for monitoring the IPv4 connectivity status.
    It provides the status of the IPv4 connection based on connectivity status.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv4 Status",
            "askey_v4_status",
            "mdi:network",
            "connect_status",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        status = "Disabled"  # Default status if not found

        if data and "status_info_v4" in data:
            statusInfoV4 = data["status_info_v4"]

            # If statusInfoV4 is a list, iterate over it
            if isinstance(statusInfoV4, list):
                for item in statusInfoV4:
                    if item.get("connectivity_type") == "1":
                        status = map_connect_status(item.get("connect_status"))
                        break
            else:
                # Fallback: If statusInfoV4 is a single object
                if statusInfoV4.get("connectivity_type") == "1":
                    status = map_connect_status(statusInfoV4.get("connect_status"))

        return status

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the current IPv4 connectivity status.",
            "Unit": "None",
        }


class AskeyConnectivityIpSensorV4(AskeyBaseSensor):
    """
    Sensor for monitoring the external IPv4 address.
    Provides the external IP address assigned to the device.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "External IPv4", "askey_v4_ip", "mdi:network", "ip"
        )

    @property
    def native_value(self):
        """Return the IP address."""
        data = self.coordinator.data
        if data and "status_info_v4" in data:
            ip = data["status_info_v4"].get("ip")
            if ip:
                return ip
        return None

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the external IPv4 address of the device.",
            "Unit": "None",
        }


class AskeyConnectivityGatewaySensorV4(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the IPv4 gateway address.
    Provides the IP address of the gateway used for routing the traffic.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv4 Gateway",
            "askey_v4_gateway",
            "mdi:router-network",
            "",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "status_info_v4" in data:
            gateway = data["status_info_v4"].get("gateway")
            if gateway:
                return gateway
        return None

    @property
    def state(self):
        return str(self.native_value) if self.native_value else None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IPv4 gateway address used for routing.",
            "Unit": "None",
        }


class AskeyConnectivityPrimaryDNSSensorV4(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Primary DNS IPv4 address.
    Provides the IP address of the primary DNS server used for name resolution.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv4 DNS 1",
            "askey_ipv4_primary_dns",
            "mdi:dns",
            "primary_dns",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "status_info_v4" in data:
            dns = data["status_info_v4"].get("primary_dns")
            if dns:
                return dns
        return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IP address of the primary DNS server for IPv4.",
            "Unit": "None",
        }


class AskeyConnectivitySecondaryDNSSensorV4(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Secondary DNS IPv4 address.
    Provides the IP address of the secondary DNS server used for name resolution.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "IPv4 DNS 2",
            "askey_v4_secondary_dns",
            "mdi:dns",
            "secondary_dns",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        if data and "status_info_v4" in data:
            dns = data["status_info_v4"].get("secondary_dns")
            if dns:
                return dns
        return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Displays the IP address of the secondary DNS server for IPv4.",
            "Unit": "None",
        }
