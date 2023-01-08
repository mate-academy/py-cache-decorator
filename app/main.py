from functools import wraps
from typing import Any


def cache(func: callable) -> callable:
    _cache = {}

    @wraps(func)
    def wrapper(*inputs: tuple) -> Any:
        if inputs not in _cache:
            _cache[inputs] = func(*inputs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return _cache[inputs]

    return wrapper
