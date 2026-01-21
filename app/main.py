from functools import wraps
from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result

    return wrapper
