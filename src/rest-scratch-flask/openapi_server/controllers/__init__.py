import os

dsfs_routing_key = os.getenv("DSFS_AMQP_ROUTING_KEY", "dsfs")
dsfs_try_exchange = f"try_{dsfs_routing_key}"
dsfs_done_exchange = f"done_{dsfs_routing_key}"
dsfs_fail_exchange = f"fail_{dsfs_routing_key}"
