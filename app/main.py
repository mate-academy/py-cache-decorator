from typing import Callable, Any
from functools import wraps


def cache(function: Callable) -> Callable:
    cache = dict()
    @wraps(function)
    def wrapper(*args) -> Any:
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = function(*args)

        return cache[args]

    return wrapper

