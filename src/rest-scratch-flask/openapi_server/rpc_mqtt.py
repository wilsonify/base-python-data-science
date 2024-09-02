import json
import logging
import os
import time
import uuid

from paho.mqtt.client import Client, MQTTv311, connack_string
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("AMQP_PORT", "1883"))
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "60"))
MQTT_USER = os.getenv("MQTT_USER", "thom")
MQTT_PASS = os.getenv("MQTT_PASS", "examplepassword")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "dsfs")


class RemoteProcedure:
    """
    sending and receiving results of a remote procedure call
    """

    def __init__(self, routing_key):
        logging.info("initialize RemoteProcedure")
        logging.info("start establishing connection")
        logging.debug(f"MQTT_HOST = {MQTT_HOST}")
        logging.debug(f"MQTT_PORT = {MQTT_PORT}")
        logging.debug(f"MQTT_TOPIC = {MQTT_TOPIC}")
        logging.debug(f"MQTT_USER = {MQTT_USER}")
        self.mqtt_client = Client(protocol=MQTTv311)
        self.qos = 0
        self.routing_key = routing_key
        self.corr_id = str(uuid.uuid4())
        self.reply_topic = f'{routing_key}_reply_{self.corr_id}'
        self.status_code = "200"
        self.response = None
        logging.debug(f"self.corr_id = {self.corr_id}")
        logging.debug(f"self.reply_topic = {self.reply_topic}")
        logging.info("start setting callback")
        self.mqtt_client.username_pw_set(username=MQTT_USER, password=MQTT_PASS)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_subscribe = self.on_subscribe
        self.mqtt_client.on_message = self.on_message
        logging.info("done setting callback")
        logging.info("done initialize RemoteProcedure")

    def on_connect(self, client, userdata, flags, rc):
        logging.info(f"Result from connect: {connack_string(rc)}")
        logging.info("start setting quality of service")
        client.subscribe(self.reply_topic, qos=0)
        logging.info("done setting quality of service")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        logging.info(f"I've subscribed with QoS: {granted_qos[0]}")

    def on_message(self, client, userdata, msg):
        """
        what to do when you get a response message
        """
        logging.debug(f"msg.topic = {msg.topic}")
        logging.debug(f"msg.mid = {msg.mid}")
        logging.debug(f"msg.qos = {msg.qos}")
        logging.debug(f"msg.properties = {msg.properties}")
        logging.debug(f"msg.payload {msg.payload}")
        if not hasattr(msg.properties, 'CorrelationData'):
            logging.warning("No correlation ID")

        if msg.properties.CorrelationData == self.corr_id:
            logging.info("correlation id matches")
            # self.response = msg.payload
        payload_bytes = msg.payload
        payload_str = msg.payload.decode("utf-8")
        payload = json.loads(payload_str)
        logging.debug("%r", f"payload={payload}")
        if isinstance(payload, dict):
            logging.debug("payload is a dict")
            if 'status_code' in self.response:
                self.status_code = payload.pop('status_code')
                logging.debug("%r", f"self.status_code={self.status_code}")
        self.response = payload

    def call(self, body_dict):
        """
        send message wait for response
        """
        logging.debug("%r", f"body_dict = {body_dict}")
        props = Properties(PacketTypes.PUBLISH)
        props.CorrelationData = self.corr_id
        props.ResponseTopic = self.reply_topic
        body_dict["reply_to"] = self.reply_topic
        body_dict["correlation_id"] = self.corr_id
        body_str = json.dumps(body_dict)
        body_bytes = body_str.encode("utf-8")
        logging.info("start opening publish connection")
        # client.tls_set()
        # client.tls_set(ca_certs=ca_certificate, certfile=client_certificate, keyfile=client_key )
        self.mqtt_client.connect(
            host=MQTT_HOST,
            port=MQTT_PORT,
            keepalive=MQTT_KEEPALIVE,
        )
        logging.info("done opening publish connection")
        self.mqtt_client.publish(
            topic=f"{self.routing_key}_try",
            payload=body_bytes,
            qos=1,
        )
        logging.info("request sent")

        logging.info("start event loop")
        self.mqtt_client.loop_start()
        logging.info("start waiting for connection")
        while not self.mqtt_client.is_connected():
            time.sleep(0.1)
        logging.info("done waiting for connection")
        logging.debug("start waiting for response")
        while self.response is None:
            time.sleep(0.1)
        logging.debug("done waiting for response")
        self.mqtt_client.loop_stop()
        logging.info("stop event loop")
        return self.response, self.status_code
