from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        ar_key = args + tuple(kwargs.values())
        if ar_key in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
        cache[ar_key] = res
        return res
    return wrapper
