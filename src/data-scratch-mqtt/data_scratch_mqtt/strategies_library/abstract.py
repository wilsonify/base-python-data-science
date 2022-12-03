import json
import logging
from types import MethodType

from data_scratch_mqtt.config import MQTT_TOPIC


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function, mqtt_client, userdata, msg):
        logging.debug("initialize Strategy")
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.mqtt_client = mqtt_client
        self.userdata = userdata
        self.msg = msg
        payload_bytes = msg.payload
        payload_str = payload_bytes.decode("utf-8")
        self.input_payload = json.loads(payload_str)
        self.reply_to = f"{MQTT_TOPIC}_reply"
        if "reply_to" in self.input_payload:
            self.reply_to = self.input_payload["reply_to"]
        self.correlation_id = "unknown"
        if "correlation_id" in self.input_payload:
            self.correlation_id = self.input_payload["correlation_id"]

    def publish(self, payload):
        payload_str = json.dumps(payload)
        payload_bytes = payload_str.encode("utf-8")
        self.mqtt_client.publish(
            topic=self.reply_to,
            payload=payload_bytes,
            qos=0
        )
