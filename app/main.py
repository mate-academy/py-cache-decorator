from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        keys = (args, tuple(sorted(kwargs.items())))
        if keys in cache_storage:
            print("Getting from cache")
            return cache_storage[keys]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[keys] = result
            return result
    return wrapper
