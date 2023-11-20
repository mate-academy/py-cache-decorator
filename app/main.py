from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_for_func = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> int:
        key_cache = args if args else kwargs
        if key_cache in cache_for_func:
            print("Getting from cache")
            result = cache_for_func[key_cache]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_for_func[key_cache] = result
        return result
    return inner
