from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_items = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, *sorted(kwargs.items()))
        if key not in cached_items:
            result = func(*args, **kwargs)
            cached_items[key] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cached_items[key]
    return wrapper
