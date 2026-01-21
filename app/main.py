from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        kv_tuple = tuple(sorted(kwargs.items()))
        _cache_key = (args, kv_tuple)
        if _cache_key in _cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            _cache[_cache_key] = func(*args, **kwargs)
        return _cache[_cache_key]
    return wrapper
