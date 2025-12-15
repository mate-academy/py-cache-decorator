from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func, args, tuple(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper
