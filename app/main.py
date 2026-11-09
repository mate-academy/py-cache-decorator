from typing import Callable

def cache(func) -> Callable:
    cache_store = {}
    def cache_wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache_store:
            print("Getting from cache")
            return cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return cache_wrapper
