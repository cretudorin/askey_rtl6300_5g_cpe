import logging

from custom_components.askey_rtl6300_5g_cpe.sensors.signal_info import (
    Askey5gRsrpSensor,
    Askey5gRsrqSensor,
    Askey5gSinrSensor,
    Askey5gPciSensor,
    Askey5gBandSensor,
    Askey5gBandwidthSensor,
    Askey5gTxPowerSensor,
    Askey5gRxChannelSensor,
    Askey5gTxChannelSensor,
    Askey5gRxFrequencySensor,
    Askey5gTxFrequencySensor,
)
from custom_components.askey_rtl6300_5g_cpe.sensors.cellular_info import (
    AskeyPccTypeSensor,
    AskeyPccGciSensor,
    AskeyPccMccSensor,
    AskeyPccMncSensor,
    AskeyPccTacSensor,
    AskeyPccEnbSensor,
    AskeyPccCqiSensor,
    AskeyPccCountSensor,
)
from custom_components.askey_rtl6300_5g_cpe.sensors.status_info import (
    AskeyNetworkNameSensor,
    AskeySignalLevelSensor,
    AskeyRoamingSensor,
)
from custom_components.askey_rtl6300_5g_cpe.sensors.traffic import (
    AskeyMonthlyRxSensor,
    AskeyMonthlyTxSensor,
    AskeyMonthlyTotalSensor,
    AskeyMonthlyUpdatedDatetimeSensor,
)

from .sensors.cellular_stats import (
    AskeyTxBytesSensor,
    AskeyRxBytesSensor,
    AskeyTxDroppedSensor,
    AskeyRxDroppedSensor,
    AskeyTxErrorSensor,
    AskeyRxErrorSensor,
    AskeyTxPacketsSensor,
    AskeyRxPacketsSensor,
)
from .sensors.pcc_cell_info import (
    AskeyPccPciSensor,
    AskeyPccRssiSensor,
    AskeyPccRsrpSensor,
    AskeyPccRsrqSensor,
    AskeyPccSinrSensor,
    AskeyPccBandSensor,
    AskeyPccBandwSensor,
    AskeyPccRxchSensor,
    AskeyPccTxchSensor,
    AskeyPccRxfreqSensor,
    AskeyPccTxfreqSensor,
)

from .sensors.scc1_cell_info import (
    AskeyScc1PciSensor,
    AskeyScc1RssiSensor,
    AskeyScc1RsrpSensor,
    AskeyScc1RsrqSensor,
    AskeyScc1SinrSensor,
    AskeyScc1BandSensor,
    AskeyScc1BandwSensor,
    AskeyScc1RxchSensor,
    AskeyScc1TxchSensor,
    AskeyScc1RxfreqSensor,
    AskeyScc1TxfreqSensor,
)

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .sensors.sms_count import AskeySmsInboxCountSensor, AskeySmsOutboxCountSensor

from .sensors.status_info_sensor_v6 import (
    AskeyConnectivityGatewaySensorV6,
    AskeyConnectivityPrimaryDNSSensorV6,
    AskeyConnectivitySecondaryDNSSensorV6,
    AskeyConnectivityStatusSensorV6,
    AskeyConnectivityIpSensorV6,
)


from .sensors.status_info_sensor_v4 import (
    AskeyConnectivityGatewaySensorV4,
    AskeyConnectivityPrimaryDNSSensorV4,
    AskeyConnectivitySecondaryDNSSensorV4,
    AskeyConnectivityStatusSensorV4,
    AskeyConnectivityIpSensorV4,
)

from .sensors.throughput_sensor import (
    AskeyThroughputDownloadSensor,
    AskeyThroughputUploadSensor,
)
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


# Setup entry for sensors
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up sensors from a config entry."""
    coordinator: DataUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    # Ensure initial data is available
    await coordinator.async_request_refresh()

    # Add all sensors
    async_add_entities(
        [
            # "Throughput"
            AskeyThroughputDownloadSensor(coordinator),
            AskeyThroughputUploadSensor(coordinator),
            # IP v6
            AskeyConnectivityStatusSensorV6(coordinator),
            AskeyConnectivityIpSensorV6(coordinator),
            AskeyConnectivityGatewaySensorV6(coordinator),
            AskeyConnectivityPrimaryDNSSensorV6(coordinator),
            AskeyConnectivitySecondaryDNSSensorV6(coordinator),
            # IP v4
            AskeyConnectivityGatewaySensorV4(coordinator),
            AskeyConnectivityPrimaryDNSSensorV4(coordinator),
            AskeyConnectivitySecondaryDNSSensorV4(coordinator),
            AskeyConnectivityStatusSensorV4(coordinator),
            AskeyConnectivityIpSensorV4(coordinator),
            # SMS
            AskeySmsInboxCountSensor(coordinator),
            AskeySmsOutboxCountSensor(coordinator),
            AskeyPccPciSensor(coordinator),
            AskeyPccRssiSensor(coordinator),
            AskeyPccRsrpSensor(coordinator),
            AskeyPccRsrqSensor(coordinator),
            AskeyPccSinrSensor(coordinator),
            AskeyPccBandSensor(coordinator),
            AskeyPccBandwSensor(coordinator),
            AskeyPccRxchSensor(coordinator),
            AskeyPccTxchSensor(coordinator),
            AskeyPccRxfreqSensor(coordinator),
            AskeyPccTxfreqSensor(coordinator),
            AskeyScc1PciSensor(coordinator),
            AskeyScc1RssiSensor(coordinator),
            AskeyScc1RsrpSensor(coordinator),
            AskeyScc1RsrqSensor(coordinator),
            AskeyScc1SinrSensor(coordinator),
            AskeyScc1BandSensor(coordinator),
            AskeyScc1BandwSensor(coordinator),
            AskeyScc1RxchSensor(coordinator),
            AskeyScc1TxchSensor(coordinator),
            AskeyScc1RxfreqSensor(coordinator),
            AskeyScc1TxfreqSensor(coordinator),
            # Traffic statistics
            AskeyTxBytesSensor(coordinator),
            AskeyRxBytesSensor(coordinator),
            AskeyTxDroppedSensor(coordinator),
            AskeyRxDroppedSensor(coordinator),
            AskeyTxErrorSensor(coordinator),
            AskeyRxErrorSensor(coordinator),
            AskeyTxPacketsSensor(coordinator),
            AskeyRxPacketsSensor(coordinator),
            AskeyMonthlyRxSensor(coordinator),
            AskeyMonthlyTxSensor(coordinator),
            AskeyMonthlyTotalSensor(coordinator),
            AskeyMonthlyUpdatedDatetimeSensor(coordinator),
            # Basic info
            AskeyPccTypeSensor(coordinator),
            AskeyPccGciSensor(coordinator),
            AskeyPccMccSensor(coordinator),
            AskeyPccMncSensor(coordinator),
            AskeyPccTacSensor(coordinator),
            AskeyPccEnbSensor(coordinator),
            AskeyNetworkNameSensor(coordinator),
            AskeySignalLevelSensor(coordinator),
            AskeyRoamingSensor(coordinator),
            # 5G
            Askey5gRsrpSensor(coordinator),
            Askey5gRsrqSensor(coordinator),
            Askey5gSinrSensor(coordinator),
            Askey5gPciSensor(coordinator),
            Askey5gBandSensor(coordinator),
            Askey5gBandwidthSensor(coordinator),
            Askey5gTxPowerSensor(coordinator),
            Askey5gRxChannelSensor(coordinator),
            Askey5gTxChannelSensor(coordinator),
            Askey5gRxFrequencySensor(coordinator),
            Askey5gTxFrequencySensor(coordinator),
            # no idea how this is calculated
            # AskeyPccServTimeSensor(coordinator),
            AskeyPccCqiSensor(coordinator),
            AskeyPccCountSensor(coordinator),
        ]
    )
