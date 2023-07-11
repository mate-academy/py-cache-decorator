from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    buffer = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in buffer:
            print("Getting from cache")
            return buffer[args]
        print("Calculating new result")
        res = func(*args)
        buffer[args] = res
        return res

    return wrapper
