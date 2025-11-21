"""
mqtt consumer
"""
import json
import logging
from logging.config import dictConfig
import os

import paho.mqtt.client as mqtt

# Import only used names from package instead of star import
from data_scratch_mqtt import (
    echo_strategy,
    mysqrt_strategy,
    mystrength_strategy,
    Strategy,
    dynamic_strategies,
    MQTT_HOST,
    MQTT_PORT,
    MQTT_KEEPALIVE,
)
from data_scratch_mqtt.config import MQTT_USER, MQTT_PASS, MQTT_TOPIC

logging_config_dict = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": """%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s | %(message)s"""
        }
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    "root": {"handlers": ["console"], "level": logging.DEBUG},
}

# Build available strategies dynamically
available_strategies = {}

# Add core strategies
available_strategies["echo"] = echo_strategy
if mysqrt_strategy is not None:
    available_strategies["sqrt"] = mysqrt_strategy
if mystrength_strategy is not None:
    available_strategies["strength"] = mystrength_strategy

# Add all dynamic strategies
available_strategies.update(dynamic_strategies)

logging.info(f"Available strategies: {len(available_strategies)} strategies loaded")


def on_connect(client, userdata, flags, rc):
    logging.info("Result from connect: {}".format(mqtt.connack_string(rc)))
    # Subscribe to the vehicles/vehiclepi01/tests topic filter
    logging.info("start setting quality of service")
    client.subscribe(MQTT_TOPIC, qos=0)
    logging.info("done setting quality of service")


def on_subscribe(client, userdata, mid, granted_qos):
    logging.info(f"I've subscribed with QoS: {granted_qos[0]}")


def on_message(client, userdata, msg):
    logging.info("Message received")
    logging.debug(f"msg.topic = {msg.topic}")
    logging.debug(f"msg.payload {msg.payload}")
    
    try:
        payload_bytes = msg.payload
        payload_str = payload_bytes.decode("utf-8")
        payload = json.loads(payload_str)
        logging.debug("%r", "payload = {}".format(payload))
        logging.debug("%r", "payload has type {}".format(type(payload)))
        
        strategy_str = payload.get("strategy", "echo")
        
        if strategy_str in available_strategies:
            selected_strategy = available_strategies[strategy_str]
            current_strategy = Strategy(selected_strategy, client, userdata, msg)
            current_strategy.execute()  # pylint:disable=not-callable
            logging.info(f"Successfully executed strategy: {strategy_str}")
        else:
            # Strategy not found - send error response
            error_response = {
                "error": f"Strategy '{strategy_str}' not found",
                "available_strategies": list(available_strategies.keys())
            }
            client.publish(
                topic=f"{MQTT_TOPIC}_reply",
                payload=json.dumps(error_response).encode("utf-8"),
                qos=0
            )
            logging.warning(f"Unknown strategy requested: {strategy_str}")
            
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        error_response = {
            "error": f"Invalid JSON in message: {str(e)}",
            "original_payload": msg.payload.decode("utf-8", errors='ignore')
        }
        client.publish(
            topic=f"{MQTT_TOPIC}_reply",
            payload=json.dumps(error_response).encode("utf-8"),
            qos=0
        )
        logging.error(f"JSON decode error: {e}")
        
    except Exception as e:
        # Handle any other errors
        error_response = {
            "error": f"Message processing failed: {str(e)}",
            "original_payload": payload_str if 'payload_str' in locals() else "unknown"
        }
        client.publish(
            topic=f"{MQTT_TOPIC}_reply",
            payload=json.dumps(error_response).encode("utf-8"),
            qos=0
        )
        logging.exception(f"Failed to consume message: {e}")
    
    logging.info("waiting for more messages")


def main():
    logging.info("main")
    logging.info("start establishing connection")
    logging.debug(f"MQTT_HOST = {MQTT_HOST}")
    logging.debug(f"MQTT_PORT = {MQTT_PORT}")
    logging.debug(f"MQTT_TOPIC = {MQTT_TOPIC}")
    logging.debug(f"MQTT_USER = {MQTT_USER}")
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    logging.info("start setting callback")
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    logging.info("done setting callback")
    logging.info("start opening channel")
    # TLS setup intentionally omitted here. If you need TLS, call
    # client.tls_set(...) with the appropriate certificates before connect.
    client.username_pw_set(username=MQTT_USER, password=MQTT_PASS)
    client.connect(
        host=MQTT_HOST,
        port=MQTT_PORT,
        keepalive=MQTT_KEEPALIVE,
    )
    logging.info("done establishing connection")
    logging.info("done opening channel")
    logging.info("python-consumer is waiting for messages")
    client.loop_forever()


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
