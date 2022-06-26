import logging
from types import MethodType


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function, channel, method, props):
        logging.debug("initialize Strategy")
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.channel = channel
        self.method = method
        self.props = props
