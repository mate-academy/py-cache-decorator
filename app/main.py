from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache: Any = {}

    @wraps(func)
    def wrapper(*args: list) -> list:
        if args in _cache:
            print("Getting from cache")
        else:
            _cache[args] = func(*args)
            print("Calculating new result")
        return _cache[args]
    return wrapper
