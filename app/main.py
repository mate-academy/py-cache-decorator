from typing import Callable


operation_cache = {}


def cache(func: Callable) -> Callable:

    cache_storage = {}
    operation_cache[func.__name__] = cache_storage

    def wrapped(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result

        return result

    return wrapped
