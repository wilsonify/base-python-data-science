"""
configuration
these are intended to be imported by many modules
"""

import logging
import os

MQTT_HOST = "10.1.1.16"
MQTT_PORT = 8883
MQTT_KEEPALIVE = 60
HOME_DIR = os.path.expanduser("~")
LOCAL_DATA_DIR = os.path.join(HOME_DIR, "repos/base-python-data-science/tests/data")
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
