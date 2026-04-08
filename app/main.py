from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    deco_cache = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = tuple(args) + tuple(kwargs.items())
        if key not in deco_cache:
            deco_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return deco_cache[key]
    return wrapper
