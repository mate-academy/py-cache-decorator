from typing import Callable, Any


def cache(func: Callable) -> Callable[..., Any]:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            return cache_dict.setdefault(key, func(*args, **kwargs))

    return wrapper
