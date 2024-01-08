from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, cache_data: dict = {}) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        cache_data[args] = func(*args)
        print("Calculating new result")
        return cache_data[args]
    return wrapper
