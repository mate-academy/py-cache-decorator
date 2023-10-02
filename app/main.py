from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args: int) -> Any:
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]
    return inner
