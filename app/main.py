from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """Decorator that caches results of a function with immutable arguments.

    Each decorated function maintains its own independent cache dictionary.
    """
    stored_results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Combine positional and keyword arguments into a hashable cache key
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    return wrapper
