import json
import logging

import pika

from data_science_from_scratch.library.probability import mysqrt


def mysqrt_strategy(self, body: dict):  # noqa: E501
    """ square root """
    logging.debug(f"body = {body}")
    logging.debug(f"type(body) = {type(body)}")
    x = body["x"]
    sqrt_output = dict(
        x=x,
        result=mysqrt(x)
    )
    self.channel.basic_publish(
        exchange='',
        routing_key=str(self.props.reply_to),
        properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
        body=json.dumps(sqrt_output).encode("utf-8")
    )


