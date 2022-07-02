import json
import logging

import pika

from data_science_from_scratch import routing_key
from data_science_from_scratch.library.probability import mysqrt


def mysqrt_strategy(self, body: dict):  # noqa: E501
    """ square root """
    logging.debug(f"body = {body}")
    logging.debug(f"type(body) = {type(body)}")
    x = body["x"]
    sqrt_output = dict(
        x=x,
        result=mysqrt(x),
        status_code="200"
    )
    logging.debug(f"sqrt_output = {sqrt_output}")
    logging.debug(f"exchange= reply_{self.props.correlation_id}")
    self.publish(sqrt_output)
