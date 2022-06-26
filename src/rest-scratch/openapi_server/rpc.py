import json
import logging
import os
import uuid

import pika

dsfs_routing_key = os.getenv("DSFS_AMQP_ROUTING_KEY", "dsfs")
dsfs_try_exchange = f"try_{dsfs_routing_key}"
dsfs_done_exchange = f"done_{dsfs_routing_key}"
dsfs_fail_exchange = f"fail_{dsfs_routing_key}"


class RemoteProcedure:
    """
    sending and receiving results of a remote procedure call
    """
    credentials = pika.PlainCredentials(
        os.getenv("AMQP_USER", "guest"),
        os.getenv("AMQP_PASS", "guest")
    )
    AMQP_HOST = os.getenv("AMQP_HOST", "localhost")
    AMQP_PORT = os.getenv("AMQP_PORT", "5672")
    heartbeat = os.getenv("AMQP_HEARTBEAT", "10000")
    timeout = os.getenv("AMQP_TIMEOUT", "10001")

    connection_parameters = pika.ConnectionParameters(
        host=AMQP_HOST,
        port=int(AMQP_PORT),  # default is 5672
        credentials=credentials,
        heartbeat=int(heartbeat),
        blocked_connection_timeout=int(timeout),
    )

    def __init__(self, routing_key):
        self.connection = pika.BlockingConnection(parameters=self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=1)
        self.routing_key = routing_key
        self.corr_id = str(uuid.uuid4())
        self.response = None

        new_queue_method_frame = self.channel.queue_declare(queue='', exclusive=True)
        self.reply_to_queue = new_queue_method_frame.method.queue
        self.properties = pika.BasicProperties(
            reply_to=self.reply_to_queue,
            correlation_id=self.corr_id,
        )
        self.declare()

    def declare(self):
        """
        make sure exchange and queue exist
        """
        route = "python"
        self.channel.exchange_declare(exchange=f"try_{route}", exchange_type="topic")
        self.channel.queue_declare(queue=f"try_{route}", durable=True, exclusive=False, auto_delete=False)
        self.channel.queue_bind(queue=f"try_{route}", exchange=f"try_{route}", routing_key=route)
        route = "dsfs"
        self.channel.exchange_declare(exchange=f"try_{route}", exchange_type="topic")
        self.channel.queue_declare(queue=f"try_{route}", durable=True, exclusive=False, auto_delete=False)
        self.channel.queue_bind(queue=f"try_{route}", exchange=f"try_{route}", routing_key=route)
        route = "tensorflow"
        self.channel.exchange_declare(exchange=f"try_{route}", exchange_type="topic")
        self.channel.queue_declare(queue=f"try_{route}", durable=True, exclusive=False, auto_delete=False)
        self.channel.queue_bind(queue=f"try_{route}", exchange=f"try_{route}", routing_key=route)

    def on_response(self, channel, method, props, body):
        """
        what to do when you get a repsponse
        """
        logging.debug("%r", f"ch={channel}")
        logging.debug("%r", f"ch={method}")

        if self.corr_id == props.correlation_id:
            self.response = json.loads(body.decode("utf-8"))

    def call(self, body_new):
        """
        send message wait for response
        """
        logging.debug("%r", f"body_new = {body_new}")

        self.channel.basic_publish(
            exchange=f'try_{self.routing_key}',
            routing_key=self.routing_key,
            body=json.dumps(body_new).encode("utf-8")
        )

        self.channel.basic_consume(
            queue=self.reply_to_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        while self.response is None:
            self.connection.process_data_events()
        return self.response
