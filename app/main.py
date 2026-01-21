from typing import Callable


def cache(func: Callable) -> Callable:
    cache_stores = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args, tuple(sorted(kwargs.items()))

        if key not in cache_stores:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_stores[key] = result
        else:
            print("Getting from cache")
            result = cache_stores[key]

        return result

    return wrapper
