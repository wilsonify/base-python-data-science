"""
mqtt consumer
"""
import json
import logging
from logging.config import dictConfig
import paho.mqtt.client as mqtt
from data_scratch_mqtt import *

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






def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    # Subscribe to the vehicles/vehiclepi01/tests topic filter
    logging.info("start setting quality of service")
    client.subscribe("vehicles/vehiclepi01/tests", qos=2)
    logging.info("done setting quality of service")


def on_subscribe(client, userdata, mid, granted_qos):
    print("I've subscribed with QoS: {}".format(granted_qos[0]))


def on_message(client, userdata, msg):
    print("Message received. Topic: {msg.topic}. Payload: {msg.payload}")
    payload = json.loads(msg.payload.decode("utf-8"))
    logging.debug("%r", "payload = {}".format(payload))
    logging.debug("%r", "payload has type {}".format(type(payload)))
    strategy_str = payload.get("strategy", "echo")
    selected_strategy = available_strategies.get(strategy_str, echo_strategy)
    current_strategy = Strategy( selected_strategy )
    try:
        current_strategy.execute(payload)  # pylint:disable=not-callable
        logging.info("done")
        # ACK on done_exchange
    except:  # pylint:disable=bare-except # noqa
        payload["status_code"] = 400
        logging.exception("failed to consume message")
        # NACK on fail_exchange
        # if properties.reply_to is not None: ACK correlation_id
        # body=json.dumps(payload).encode("utf-8")
    logging.info("waiting for more messages")

    


def main():
    logging.info("main")
    logging.info("start establishing connection")
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    logging.info("start setting callback")
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    logging.info("done setting callback")

    logging.info("start opening channel")
    #client.tls_set(ca_certs=ca_certificate, certfile=client_certificate, keyfile=client_key    )
    client.connect( host=MQTT_HOST, port=MQTT_PORT, keepalive=MQTT_KEEPALIVE )
    logging.info("done establishing connection")
    logging.info("done opening channel")    

    logging.info("python-consumer is waiting for messages")
    client.loop_forever()


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
