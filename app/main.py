from collections.abc import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    _cache = {}

    def wrapper(*args) -> Any:
        if args not in _cache:
            _cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return _cache[args]
    return wrapper
