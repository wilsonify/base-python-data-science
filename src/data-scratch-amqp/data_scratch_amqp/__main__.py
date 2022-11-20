"""
amqp consumer
"""
import json
import logging
import os
from logging.config import dictConfig
import pika
from data_scratch_amqp import *

logging.getLogger(__name__).addHandler(logging.NullHandler())
amqp_host = os.getenv("AMQP_HOST", "localhost")
amqp_port = os.getenv("AMQP_PORT", "5672")
routing_key = os.getenv("AMQP_ROUTING_KEY", "dsfs")
heartbeat = os.getenv("AMQP_HEARTBEAT", "10000")
timeout = os.getenv("AMQP_TIMEOUT", "10001")
cred = pika.PlainCredentials(
    os.getenv("AMQP_USER", "guest"),
    os.getenv("AMQP_PASS", "guest")
)
try_exchange = f"try_{routing_key}"
done_exchange = f"done_{routing_key}"
fail_exchange = f"fail_{routing_key}"

logging_config_dict = dict(
    version=1,
    formatters={"simple": {"format": """%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s | %(message)s"""}},
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)

available_strategies = dict(
    echo=echo_strategy,
    sqrt=mysqrt_strategy,
    strength=mystrength_strategy,
    difference_quotient=difference_quotient,
    estimate_gradient=estimate_gradient,
    in_random_order=in_random_order,
    maximize_batch=maximize_batch,
    maximize_stochastic=maximize_stochastic,
    minimize_batch=minimize_batch,
    minimize_stochastic=minimize_stochastic,
    partial_difference_quotient=partial_difference_quotient,
    distance=distance,
    dot=dot,
    get_column=get_column,
    get_row=get_row,
    magnitude=magnitude,
    matrix_add=matrix_add,
    scalar_multiply=scalar_multiply,
    shape=shape,
    squared_distance=squared_distance,
    sum_of_squares=sum_of_squares,
    vector_add=vector_add,
    vector_mean=vector_mean,
    vector_subtract=vector_subtract,
    vector_sum=vector_sum,
    accuracy=accuracy,
    precision=precision,
    recall=recall,
    f1_score=f1_score,
    split_data=split_data,
    train_test_split=train_test_split,
    bucketize=bucketize,
    correlation=correlation,
    correlation_matrix=correlation_matrix,
    covariance=covariance,
    data_range=data_range,
    de_mean=de_mean,
    interquartile_range=interquartile_range,
    mean=mean,
    median=median,
    mode=mode,
    quantile=quantile,
    standard_deviation=standard_deviation,
    variance=variance,
    bernoulli_trial=bernoulli_trial,
    binomial=binomial,
    inverse_normal_cdf=inverse_normal_cdf,
    normal_cdf=normal_cdf,
    normal_pdf=normal_pdf,
    random_kid=random_kid,
    uniform_cdf=uniform_cdf,
    uniform_pdf=uniform_pdf,

)


def route_callback(ch, method, properties, body):
    logging.info("route_callback")
    logging.debug("%r", "ch={}".format(ch))
    logging.debug("%r", "properties={}".format(properties))
    logging.debug("%r", "key={}".format(routing_key))
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


connection_parameters = pika.ConnectionParameters(
    host=amqp_host,
    port=int(amqp_port),
    heartbeat=int(heartbeat),
    blocked_connection_timeout=int(timeout),
    credentials=cred,
)


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
