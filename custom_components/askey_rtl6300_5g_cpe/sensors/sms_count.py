from custom_components.askey_rtl6300_5g_cpe.utils import safe_get_property
from .base_sensor import AskeyBaseSensor
import logging

_LOGGER = logging.getLogger(__name__)


class AskeySmsInboxCountSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the SMS inbox count of ASKEY device.
    This sensor tracks the total number of messages in the inbox.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            name="SMS Inbox Count",
            unique_id="askey_sms_inbox_count",
            icon="mdi:message-text",
            value_key="inbox_count",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["sms_inbox_count", "totalcount"]
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Total number of messages in the SMS inbox.",
            "Unit": "messages",
        }


class AskeySmsOutboxCountSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the SMS outbox count of ASKEY device.
    This sensor tracks the total number of messages in the outbox.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            name="SMS Outbox Count",
            unique_id="askey_sms_outbox_count",
            icon="mdi:message-text",
            value_key="outbox_count",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["sms_outbox_count", "totalcount"]
        )

    @property
    def extra_state_attributes(self):

        return {
            "Description": "Total number of messages in the SMS outbox.",
            "Unit": "messages",
        }
