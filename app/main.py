from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        if (args, frozenset(kwargs.items())) in _cache:
            print("Getting from cache")
            return _cache[(args, frozenset(kwargs.items()))]

        print("Calculating new result")
        result = func(*args, **kwargs)
        _cache[(args, frozenset(kwargs.items()))] = result
        return result

    return wrapper
