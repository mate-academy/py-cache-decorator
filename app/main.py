from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_item = {}

    @wraps(func)
    def wrapper(*args) -> Any:

        if args not in cache_item.keys():
            cache_item[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_item[args]
    return wrapper
