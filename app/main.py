from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        cached_key = f"{args} - {tuple(sorted(kwargs.items()))}"
        if cached_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cached_key]
        print("Calculating new result")
        res = func(*args, **kwargs)
        cache_dict[cached_key] = res
        return res

    return wrapper
