import logging

from dsl.c06_probability.probability import mysqrt


def mysqrt_strategy(self, body: dict):  # noqa: E501
    """ square root """
    logging.debug(f"body = {body}")
    logging.debug(f"type(body) = {type(body)}")
    x = body["x"]
    result = mysqrt(x)
    result = round(result, 4)
    sqrt_output = dict(x=x, result=result)
    logging.debug(f"sqrt_output = {sqrt_output}")
    self.publish(sqrt_output)
