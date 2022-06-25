import json
import logging

import pika


def echo(self, payload):
    logging.info(f"payload = {payload}")
    self.channel.basic_publish(
        exchange='',
        routing_key=str(self.props.reply_to),
        properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
        body=json.dumps(payload).encode("utf-8")
    )
