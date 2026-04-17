from functools import wraps
from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper
