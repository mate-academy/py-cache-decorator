from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}
    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache_data.keys():
            cache_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_data[args]

    return wrapper
