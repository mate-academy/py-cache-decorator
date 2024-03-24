from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    new_cache = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in new_cache:
            print("Calculating new result")
            result = func(*args)
            new_cache[args] = result

        else:
            print("Getting from cache")

        return new_cache[args]

    return wrapper
