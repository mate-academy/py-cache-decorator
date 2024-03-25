from typing import Callable

def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args, **kwargs):
        nonlocal result_cache
        key = (args, frozenset(kwargs.items()))
        if key in result_cache:
            print("Getting from cache")
            return result_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            result_cache[key] = result
            return result

    return wrapper
