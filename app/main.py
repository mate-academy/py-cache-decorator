from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    wrapper_cache = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in wrapper_cache:
            wrapper_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return wrapper_cache[args]

    return wrapper
