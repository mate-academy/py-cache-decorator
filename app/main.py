from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cache_key] = result

        return result

    return wrapper
