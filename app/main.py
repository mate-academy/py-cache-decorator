from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_for_func = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> int:
        key_cache = (args, tuple(kwargs.items()))
        if key_cache in cache_for_func:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_for_func[key_cache] = func(*args, **kwargs)
        return cache_for_func[key_cache]
    return inner
