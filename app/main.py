from typing import Callable, Any
from functools import wraps

def cache(func: Callable) -> Callable:
    cached = []
    arg_cache = []

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal cached, arg_cache

        if args not in arg_cache:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached.append(result)
            arg_cache.append(args)

            return result

        else:
            print("Getting from cache")

        return cached[arg_cache.index(args)]

    return wrapper
