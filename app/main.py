from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        if not cache_data.get(func.__name__):
            result = func(*args)
            cache_data[func.__name__] = {}
            cache_data[func.__name__][args] = result
            print("Calculating new result")
            return result
        elif cache_data.get(func.__name__).get(args) is None:
            result = func(*args)
            cache_data[func.__name__][args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cache_data[func.__name__][args]
    return inner
