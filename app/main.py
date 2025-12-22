from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in stored_cache:
            print("Getting from cache")
            return stored_cache[key]
        else:
            print("Calculating new result")
            stored_cache[key] = func(*args, **kwargs)
            return stored_cache[key]

    return wrapper
