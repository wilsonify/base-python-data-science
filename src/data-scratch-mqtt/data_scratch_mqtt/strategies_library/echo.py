import logging


def echo_strategy(self, payload):
    logging.info(f"payload = {payload}")
    self.publish(payload)
