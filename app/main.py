from functools import wraps
from typing import Callable, Any


cache_dict = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any) -> int:
        if func not in cache_dict:
            cache_dict[func] = {}
        if args not in cache_dict[func]:
            print("Calculating new result")
            cache_dict[func][args] = func(*args)
        else:
            print("Getting from cache")

        return cache_dict[func][args]

    return wrapper
