from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in cached_data:
            print("Getting from cache")

            return cached_data[args]

        print("Calculating new result")

        result = func(*args)
        cached_data[args] = result

        return result

    return inner
