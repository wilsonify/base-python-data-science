import logging
from logging.config import dictConfig

from dsl.c11_machine_learning.machine_learning import accuracy, precision, f1_score, recall


def main():
    logging.info("%r", f"accuracy(70, 4930, 13930, 981070) {accuracy(70, 4930, 13930, 981070)}")
    logging.info("%r", f"precision(70, 4930, 13930, 981070) {precision(70, 4930, 13930, 981070)}")
    logging.info("%r", f"recall(70, 4930, 13930, 981070) {recall(70, 4930, 13930, 981070)}")
    logging.info("%r", f"f1_score(70, 4930, 13930, 981070) {f1_score(70, 4930, 13930, 981070)}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
