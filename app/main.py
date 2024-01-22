from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        else:
            result = func(*args, **kwargs)
            cache_store[key] = result
            print("Calculating new result")
            return result

    return wrapper
