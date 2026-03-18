from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in saved_results:
            print("Getting from cache")
            return saved_results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_results[cache_key] = result
        return result

    return wrapper