from typing import Callable, Any

cache_dict = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (func, args, tuple(sorted(kwargs.items())))
        if cache_key not in cache_dict:
            res = func(*args, **kwargs)
            cache_dict[cache_key] = res
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return cache_dict[cache_key]

    return wrapper
