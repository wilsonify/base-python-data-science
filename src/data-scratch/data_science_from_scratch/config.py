"""
configuration
these are intended to be imported by many modules
"""

import logging

AMQP_HOST = "10.1.1.16"
AMQP_PORT = 5672

LOGGING_LEVEL = logging.DEBUG
LOGGING_CONFIG_DICT = dict(
    version=1,
    formatters={
        "simple": {
            "format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""
        }
    },
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)
