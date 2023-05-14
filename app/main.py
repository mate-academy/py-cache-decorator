from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    all_results = {}

    @wraps(func)
    def decorated_function(*args, **kwargs) -> Callable:
        cache_key = (func.__name__, args)
        available_in_cache = all_results.get(cache_key, None)
        if available_in_cache is not None:
            print("Getting from cache")
            return available_in_cache
        print("Calculating new result")
        result = func(*args, **kwargs)
        all_results[cache_key] = result

        return result

    return decorated_function
