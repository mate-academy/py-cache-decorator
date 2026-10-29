from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args, **kwargs) -> Any:
        args_key = (args, frozenset(kwargs.items()))

        if args_key in cache_storage:
            print("Getting from cache")
            return cache_storage[args_key]

        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[args_key] = result
            return result

    return inner
