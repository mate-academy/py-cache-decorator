from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Any:
        current_func = args
        if current_func in cache_storage:
            print("Getting from cache")
            return cache_storage[current_func]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[current_func] = result
            return result
    return wrapper
