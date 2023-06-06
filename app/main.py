from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cache_list:
            print("Getting from cache")
            return cache_list[args]
        cache_list[args] = func(*args, **kwargs)
        print("Calculating new result")
        return cache_list[args]
    return wrapper
