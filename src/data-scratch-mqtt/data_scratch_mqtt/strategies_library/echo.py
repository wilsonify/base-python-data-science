import logging


def echo_strategy(self):
    logging.info(f"payload = {self.input_payload}")
    self.publish(self.input_payload)
