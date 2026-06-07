from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    func_cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[cache_key] = result
            return result
    return wrapper
