from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> int:
        key = (args, tuple(kwargs))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache[key]

    return wrapper
