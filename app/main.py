import inspect
from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        bound_args = sig.bind(*args, **kwargs)

        bound_args.apply_defaults()
        cache_key = tuple(bound_args.arguments.items())

        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cache_key] = result

        return result

    return wrapper
