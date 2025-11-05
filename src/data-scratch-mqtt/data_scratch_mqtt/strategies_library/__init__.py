from data_scratch_mqtt.strategies_library.abstract import Strategy
from data_scratch_mqtt.strategies_library.echo import echo_strategy

# Try to import optional strategies that may have missing dependencies
try:
    from data_scratch_mqtt.strategies_library.mysqrt import mysqrt_strategy
except ImportError:
    mysqrt_strategy = None

try:
    from data_scratch_mqtt.strategies_library.mystrength import mystrength_strategy
except ImportError:
    mystrength_strategy = None

# Import all dynamic strategies
try:
    from data_scratch_mqtt.strategies_library.dynamic_strategy import dynamic_strategies
    # Add all dynamic strategies to the module namespace
    globals().update(dynamic_strategies)
except ImportError:
    dynamic_strategies = {}
