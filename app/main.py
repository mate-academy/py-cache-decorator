from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs):
        function_calling = (func.__name__, args, frozenset(kwargs.items()))
        if function_calling in cache:
            print("Getting from cache")
            return cache[function_calling]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[function_calling] = result
            return result
    return wrapper
