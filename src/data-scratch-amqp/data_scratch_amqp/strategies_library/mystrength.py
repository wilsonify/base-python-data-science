from dsl.c06_probability.probability import mystrength


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
    self.publish(out_dict)
