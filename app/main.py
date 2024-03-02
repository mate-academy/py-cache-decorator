from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func, args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            cache_dict[key] = result
            return result

    return wrapper
