from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if cached.get(args, None) is None:
            cached[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached[args]
    return wrapper
