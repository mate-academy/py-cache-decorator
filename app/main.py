from typing import Callable


def cache(func: Callable) -> Callable:

    cache_storage = {}

    def wrapper(*args, **kwargs) -> int:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[args] = result
            return result

    return wrapper
