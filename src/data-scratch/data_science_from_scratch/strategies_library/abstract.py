from types import MethodType


class Strategy:
    """The Strategy Pattern class"""
    def __init__(self, function, channel, method, props):
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)
        self.channel = channel
        self.method = method
        self.props = props
        self.reply_to = props.reply_to
        self.correlation_id = props.correlation_id

