import logging

from dsl.probability import mystrength


def mystrength_strategy(self, body: dict):  # noqa: E501
    """ signal strength """
    actual = body["actual"]
    expected = body["expected"]
    strength = mystrength(actual, expected)
    out_dict = dict(
        actual=actual,
        expected=expected,
        strength=round(strength, 4),
        status_code="200"
    )
    logging.debug(f"out_dict = {out_dict}")
    self.publish(out_dict)
