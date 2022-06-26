import json

import pika

from data_science_from_scratch import routing_key
from data_science_from_scratch.library.probability import mystrength


def mystrength_strategy(self, body: dict):  # noqa: E501
    """ signal strength """
    actual = body["actual"]
    expected = body["expected"]
    strength = mystrength(actual, expected)
    out_dict = dict(
        actual=actual,
        expected=expected,
        strength=strength,
        status_code="200"
    )
    self.channel.basic_publish(
        exchange=self.props.reply_to,
        routing_key=routing_key,
        properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
        body=json.dumps(out_dict).encode("utf-8")
    )
