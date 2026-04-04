from typing import Callable
import functools


def cache(func: Callable) -> Callable[..., None]:
    local_cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in local_cache:
            print("Getting from cache")
            return local_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            local_cache[key] = result
            return result
    return wrapper
