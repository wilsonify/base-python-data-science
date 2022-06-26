import json
import logging

import pika

from data_science_from_scratch import routing_key


def echo_strategy(self, payload):
    logging.info(f"payload = {payload}")
    self.channel.basic_publish(
        exchange=self.props.reply_to,
        routing_key=routing_key,
        properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
        body=json.dumps(payload).encode("utf-8")
    )
