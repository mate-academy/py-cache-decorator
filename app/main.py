from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> Any:
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        return cache_dict[args]
    return inner
