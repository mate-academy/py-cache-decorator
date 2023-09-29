from typing import Callable



def cache(func: Callable) -> Callable:
    from functools import wraps
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            print("Calculating new result")
            return result

    return wrapper
