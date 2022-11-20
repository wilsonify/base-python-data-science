import json
import logging
from types import MethodType

import pika



class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function, channel, method, props):
        logging.debug("initialize Strategy")
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.channel = channel
        self.method = method
        self.props = props

    def publish(self, payload):
        self.channel.basic_publish(
            exchange=self.props.reply_to,
            routing_key=routing_key,
            properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
            body=json.dumps(payload).encode("utf-8")
        )
