from typing import Callable, Any
from functools import wraps

def cache(func: Callable) -> Callable:
    cache_map: dict = {}
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_map:
            print("Getting from cache")
            return cache_map[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_map[key] = result
        return result
    return wrapper
