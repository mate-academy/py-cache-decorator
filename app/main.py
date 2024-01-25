from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_list = {}

    def wrapper(*args) -> Any:
        if args in cache_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_list[args] = func(*args)
        return cache_list[args]
    return wrapper
