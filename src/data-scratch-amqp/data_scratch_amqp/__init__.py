import os

from data_scratch_amqp.strategies_library import Strategy
from data_scratch_amqp.strategies_library import echo_strategy

# Try to import optional strategies that may have missing dependencies
try:
    from data_scratch_amqp.strategies_library import mysqrt_strategy
except ImportError:
    mysqrt_strategy = None

try:
    from data_scratch_amqp.strategies_library import mystrength_strategy
except ImportError:
    mystrength_strategy = None

# Import all dynamic strategies
try:
    from data_scratch_amqp.strategies_library.dynamic_strategy import dynamic_strategies
    # Add all dynamic strategies to the module namespace
    globals().update(dynamic_strategies)
except ImportError:
    dynamic_strategies = {}

amqp_host = os.getenv("AMQP_HOST", "localhost")
amqp_port = os.getenv("AMQP_PORT", "5672")
routing_key = os.getenv("AMQP_ROUTING_KEY", "dsfs")
heartbeat = os.getenv("AMQP_HEARTBEAT", "10000")
timeout = os.getenv("AMQP_TIMEOUT", "10001")
