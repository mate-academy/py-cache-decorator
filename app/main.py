from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    buffer = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if (args, tuple(kwargs.items())) in buffer:
            print("Getting from cache")
            return buffer[args, tuple(kwargs.items())]
        print("Calculating new result")
        result = func(*args, **kwargs)
        buffer[args, tuple(kwargs.items())] = result
        return result

    return inner
