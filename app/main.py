from typing import Callable, Dict, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict: Dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        key = (args, tuple(sorted((k, v) for k, v in kwargs.items())))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        print("Calculating new result")
        return result

    return wrapper
