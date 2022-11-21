import json
import logging
from types import MethodType


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function, mqtt_client):
        logging.debug("initialize Strategy")
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.mqtt_client = mqtt_client
        self.reply_to = None
        self.correlation_id = None

    def publish(self, payload):
        self.mqtt_client.publish(
            self.reply_to,
            body=json.dumps(payload).encode("utf-8")
        )
