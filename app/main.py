from typing import Callable, Any


def cache(func: Callable) -> [Callable]:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[key]
    return wrapper
