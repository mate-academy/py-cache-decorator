from typing import Callable, Any
from functools import wraps

def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, *kwargs, *kwargs.values())

        if cache_key not in cached_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data[cache_key] = result

            return result
        else:
            print("Getting from cache")
            return cached_data[cache_key]

    return wrapper
