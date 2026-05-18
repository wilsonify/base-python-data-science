import importlib
import inspect
import logging
from typing import Any, Dict

from common.dynamic_strategy_shared import (
    _build_kwargs,
    _create_strategies,
    _populate_module_mappings,
    _publish_error,
)


def create_dynamic_strategy(module_path: str, function_name: str):
    """Create a dynamic strategy function that wraps a library function."""

    def dynamic_strategy(self):
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)
            sig = inspect.signature(func)
            kwargs = _build_kwargs(sig, getattr(self, "input_payload", {}))
            result = func(**kwargs)
            try:
                self.publish(result)
            except Exception:
                logging.exception("Failed to publish dynamic strategy result")
        except Exception as exc:
            _publish_error(self, exc, function_name, module_path)

    dynamic_strategy.__name__ = f"{function_name}_strategy"
    return dynamic_strategy


def get_all_library_functions() -> Dict[str, Any]:
    module_mappings: Dict[str, str] = {}
    _populate_module_mappings(module_mappings)
    return _create_strategies(module_mappings, create_dynamic_strategy)


dynamic_strategies = get_all_library_functions()
