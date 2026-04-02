from typing import Callable, Any
import inspect


def cache(func: Callable) -> Callable:
    stored_dict = {}
    sig = inspect.signature(func)

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        key = tuple(bound.arguments.items())
        if key in stored_dict:
            print("Getting from cache")
            return stored_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_dict[key] = result
            return result
    return wrapper
