from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_storage = {}
    def inner(*args, **kwargs) -> Any:
        if kwargs:
            key = (args, frozenset(kwargs.items()))
        else:
            key = args
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            result = func(*args, **kwargs)
            cache_storage[key] = result
            print("Calculating new result")
            return result
    return inner




