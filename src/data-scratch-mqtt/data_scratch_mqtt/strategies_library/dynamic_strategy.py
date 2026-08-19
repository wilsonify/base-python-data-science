import importlib
import inspect
import logging
from typing import Any, Dict


def _build_kwargs_local(sig: inspect.Signature, source: Dict[str, Any]) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {}
    for param, param_obj in sig.parameters.items():
        if param in source:
            kwargs[param] = source[param]
        elif param_obj.default != inspect.Parameter.empty:
            kwargs[param] = param_obj.default
    return kwargs


def _publish_error_local(publisher, exc: Exception, fn: str, mod: str) -> None:
    try:
        publisher.publish({"error": str(exc), "function": fn, "module": mod})
    except Exception:
        logging.exception("Failed to publish error: %s", exc)


try:
    from common.dynamic_strategy_shared import (
        _build_kwargs,
        _create_strategies,
        _populate_module_mappings,
        _publish_error,
    )
except ImportError:
    _build_kwargs = _build_kwargs_local
    _publish_error = _publish_error_local

    def _populate_module_mappings(module_mappings: Dict[str, str]) -> None:
        import pkgutil
        try:
            import dsl
        except ImportError:
            return
        for importer, modname, ispkg in pkgutil.walk_packages(
            dsl.__path__, dsl.__name__ + "."
        ):
            if ispkg or "test" in modname.lower():
                continue
            try:
                mod = importlib.import_module(modname)
                for name, obj in inspect.getmembers(mod, inspect.isfunction):
                    if obj.__module__ == modname:
                        module_mappings[name] = modname
            except Exception:
                continue

    def _create_strategies(
        module_mappings: Dict[str, str], strategy_factory
    ) -> Dict[str, Any]:
        strategies: Dict[str, Any] = {}
        for func_name, module_path in module_mappings.items():
            strategies[func_name] = strategy_factory(module_path, func_name)
        return strategies


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
    if _populate_module_mappings is None or _create_strategies is None:
        return {}
    module_mappings: Dict[str, str] = {}
    _populate_module_mappings(module_mappings)
    return _create_strategies(module_mappings, create_dynamic_strategy)


dynamic_strategies = get_all_library_functions()
