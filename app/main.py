from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_info = {}

    def wrapper(*args, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_info:
            print("Getting from cache")
            return cache_info[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_info[key] = result
            return result

    return wrapper
