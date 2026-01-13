from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if (args, tuple(kwargs.items())) in cache_storage:
            print("Getting from cache")
            return cache_storage[args, tuple(kwargs.items())]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[args, tuple(kwargs.items())] = result
            return result

    return wrapper
