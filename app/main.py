from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]
    cache_dict = dict()
    return wrapper
