import json
import logging

import pika

from data_science_from_scratch import routing_key


def echo_strategy(self, payload):
    logging.info(f"payload = {payload}")
    self.publish(payload)
