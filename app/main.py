from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_res = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args if not kwargs else (args, tuple(sorted(kwargs.items())))

        if key in cache_res:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_res[key] = func(*args, **kwargs)

        return cache_res[args]

    return wrapper
