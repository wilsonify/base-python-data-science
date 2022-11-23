import json
import logging
from types import MethodType

from data_scratch_mqtt.config import MQTT_TOPIC


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function, mqtt_client):
        logging.debug("initialize Strategy")
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.mqtt_client = mqtt_client
        self.reply_to = f"{MQTT_TOPIC}_reply"
        self.correlation_id = None

    def publish(self, payload):
        payload_str = json.dumps(payload)
        payload_bytes = payload_str.encode("utf-8")
        self.mqtt_client.publish(
            topic=self.reply_to,
            payload=payload_bytes,
            qos=0
        )
