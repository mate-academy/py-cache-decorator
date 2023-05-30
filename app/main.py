from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> Any:
        key = args
        if key in cached_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_data[key] = func(*args)
        return cached_data[key]
    return wrapper
