"""
amqp consumer
"""
import json
import logging
from logging.config import dictConfig

import pika

import data_science_from_scratch
from data_science_from_scratch import routing_key, try_exchange, done_exchange, fail_exchange, connection_parameters

from data_science_from_scratch.strategies_library import (
    Strategy,
    echo_strategy,
    mysqrt_strategy,
    mystrength_strategy
)

logging_config_dict = dict(
    version=1,
    formatters={
        "simple": {
            "format": """%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s | %(message)s"""
        }
    },
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)

available_strategies = dict(
    echo=echo_strategy,
    sqrt=mysqrt_strategy,
    strength=mystrength_strategy

)


def route_callback(ch, method, properties, body):
    logging.info("route_callback")
    logging.debug("%r", "ch={}".format(ch))
    logging.debug("%r", "properties={}".format(properties))
    logging.debug("%r", "key={}".format(data_science_from_scratch.routing_key))
    logging.debug("%r", "body={}".format(body))
    logging.debug("%r", "body has type {}".format(type(body)))
    payload = json.loads(body.decode("utf-8"))
    logging.debug("%r", "payload = {}".format(payload))
    logging.debug("%r", "payload has type {}".format(type(payload)))
    if properties.reply_to is not None:
        logging.debug("%r", f"properties.correlation_id = {properties.correlation_id}")
        logging.debug("%r", f"properties.reply_to = {properties.reply_to}")

    strategy_str = payload.get('strategy', 'echo')
    selected_strategy = available_strategies.get(strategy_str, echo_strategy)
    current_strategy = Strategy(selected_strategy, channel=ch, method=method, props=properties)
    # noinspection PyBroadException
    try:
        current_strategy.execute(payload)  # pylint:disable=not-callable
        logging.info("done")
        ch.basic_publish(
            exchange=done_exchange,
            routing_key=routing_key,
            properties=properties,
            body=body
        )
    except:  # pylint:disable=bare-except # noqa

        payload['status_code'] = 400
        logging.exception("failed to consume message")
        ch.basic_publish(
            exchange=fail_exchange,
            routing_key=routing_key,
            properties=properties,
            body=body
        )
        if properties.reply_to is not None:
            ch.basic_publish(
                exchange=properties.reply_to,
                routing_key=routing_key,
                properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                body=json.dumps(payload).encode('utf-8')
            )
    logging.info("waiting for more messages")


def main():
    logging.info("main")
    logging.info("start establishing connection")
    connection = pika.BlockingConnection(connection_parameters)
    logging.info("done establishing connection")

    logging.info("start opening channel")
    channel = connection.channel()
    logging.info("done opening channel")

    logging.info("start setting quality of service")
    channel.basic_qos(prefetch_count=1)
    logging.info("done setting quality of service")

    logging.info("start declaring exchange")
    channel.exchange_declare(exchange=try_exchange, exchange_type="topic")
    channel.exchange_declare(exchange=done_exchange, exchange_type="topic")
    channel.exchange_declare(exchange=fail_exchange, exchange_type="topic")
    logging.info("done declaring exchange")

    logging.info("start declaring queues")
    channel.queue_declare(try_exchange, durable=True, exclusive=False, auto_delete=False)
    channel.queue_declare(done_exchange, durable=True, exclusive=False, auto_delete=False)
    channel.queue_declare(fail_exchange, durable=True, exclusive=False, auto_delete=False)
    logging.info("done declaring queues")

    logging.info("start binding queues")
    channel.queue_bind(queue=try_exchange, exchange=try_exchange, routing_key=routing_key)
    channel.queue_bind(queue=done_exchange, exchange=done_exchange, routing_key=routing_key)
    channel.queue_bind(queue=fail_exchange, exchange=fail_exchange, routing_key=routing_key)
    logging.info("done binding queues")

    logging.info("start setting callback")
    channel.basic_consume(
        queue=try_exchange,
        on_message_callback=route_callback,
        auto_ack=True
    )
    logging.info("done setting callback")

    logging.info("python-consumer is waiting for messages")
    channel.start_consuming()


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
