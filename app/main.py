import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    wrapper.cache = stored_results
    return wrapper