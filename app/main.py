from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_result = {}

    def wrapper(*args) -> Any:
        if isinstance(args, (dict, set, list)) is False:
            if args in cache_result:
                print("Getting from cache")
                return cache_result[args]
        cache_result[args] = func(*args)
        print("Calculating new result")
        return cache_result[args]
    return wrapper
