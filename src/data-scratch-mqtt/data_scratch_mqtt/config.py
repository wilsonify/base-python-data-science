import logging
import os

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "60"))
MQTT_USER = os.getenv("MQTT_USER", "")
MQTT_PASS = os.getenv("MQTT_PASS", "")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "dsfs")
LOCAL_DATA_DIR = os.getenv("LOCAL_DATA_DIR", os.path.join(os.path.dirname(__file__), "data"))
LOGGING_LEVEL = logging.DEBUG
LOGGING_CONFIG_DICT = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"
        }
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    "root": {"handlers": ["console"], "level": logging.DEBUG},
}
