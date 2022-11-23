import json
import logging

import paho.mqtt.client as mqtt
import pytest

from data_scratch_mqtt.config import MQTT_TOPIC, MQTT_USER, MQTT_PASS, MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE


def on_connect(client, userdata, flags, rc):
    print(f"Result from connect: {mqtt.connack_string(rc)}")
    # Subscribe to the vehicles/vehiclepi01/tests topic filter
    logging.info("start setting quality of service")
    client.subscribe(MQTT_TOPIC, qos=0)
    logging.info("done setting quality of service")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"I've subscribed with QoS: {granted_qos[0]}")


def on_message(client, userdata, msg):
    print(f"Message received. Topic: {msg.topic}. Payload: {msg.payload}")
    payload = json.loads(msg.payload.decode("utf-8"))
    logging.debug("%r", "payload = {}".format(payload))
    logging.debug("%r", "payload has type {}".format(type(payload)))


@pytest.fixture(name="mqtt_client")
def mqtt_client_fixture():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    logging.info("start setting callback")
    client.on_connect = on_connect
    # client.on_subscribe = on_subscribe
    # client.on_message = on_message
    logging.info("done setting callback")
    logging.info("start opening channel")
    # client.tls_set()
    # client.tls_set(ca_certs=ca_certificate, certfile=client_certificate, keyfile=client_key )
    client.username_pw_set(
        username=MQTT_USER,
        password=MQTT_PASS
    )
    client.connect(
        host=MQTT_HOST,
        port=MQTT_PORT,
        keepalive=MQTT_KEEPALIVE,
    )
    logging.info("done establishing connection")
    logging.info("done opening channel")
    return client
