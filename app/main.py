from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = []
    arg_cache = []
    kwargs_cache = []

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal cached, arg_cache, kwargs_cache

        if cached is None or args not in arg_cache or \
                kwargs not in kwargs_cache:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached.append(result)
            arg_cache.append(args)
            kwargs_cache.append(kwargs)

            return result

        else:
            print("Getting from cache")

        return cached[arg_cache.index(args)]

    return wrapper
