from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args, **kwargs) -> Callable:
        args_hash = (args, tuple(sorted(kwargs.items())))
        func_hash = func.__hash__()
        key = (args_hash, func_hash)
        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return inner
