from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def inner(*args) -> Any:
        cached_key = (func, args)
        if cache_storage.get(cached_key) is None:
            cache_storage[cached_key] = func(*args)
            print("Calculating new result")
            return cache_storage[cached_key]

        print("Getting from cache")
        return cache_storage.get(cached_key)

    return inner
