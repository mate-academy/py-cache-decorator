from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (tuple(args), tuple(sorted(kwargs.items())))
        if cache_key in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[cache_key]
    return wrapper
