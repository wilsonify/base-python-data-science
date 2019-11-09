import logging
import os

host = "10.1.1.16"
port = 5672

logging_dir = "logs"
logging_level = logging.DEBUG
logging_file_name = "base-python-data-science.log"
logging_config_dict = dict(
    version=1,
    formatters={
        "simple": {"format": """%(asctime)s %(name)-12s %(levelname)-8s %(message)s"""}
    },
    handlers={
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(logging_dir, logging_file_name),
            "formatter": "simple",
        },
    },
    root={"handlers": ["console", "file"], "level": logging_level},
)
