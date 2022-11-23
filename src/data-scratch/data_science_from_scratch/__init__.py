import os

import pika


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
connection_parameters = pika.ConnectionParameters(
    host=amqp_host,
    port=int(amqp_port),
    heartbeat=int(heartbeat),
    blocked_connection_timeout=int(timeout),
    credentials=cred,
)
