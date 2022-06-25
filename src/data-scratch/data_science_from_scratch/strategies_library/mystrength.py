import json

import pika

from data_science_from_scratch.library.probability import mystrength


def mystrength_strategy(self, body: dict):  # noqa: E501
    """ signal strength """
    actual = body["actual"]
    expected = body["expected"]
    strength = mystrength(actual, expected)
    out_dict = dict(
        actual=actual,
        expected=expected,
        strength=strength
    )
    self.channel.basic_publish(
        exchange='',
        routing_key=str(self.props.reply_to),
        properties=pika.BasicProperties(correlation_id=self.props.correlation_id),
        body=json.dumps(out_dict).encode("utf-8")
    )
