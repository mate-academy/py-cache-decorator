from typing import Callable
from functools import wraps
from typing import Any

def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in result:
            print("Getting from cache")
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key]

    return wrapper
