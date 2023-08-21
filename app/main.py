from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        if (args, tuple(kwargs.items())) in cache_dict:
            print("Getting from cache")
            return cache_dict[(args, tuple(kwargs.items()))]
        else:
            print("Calculating new result")
            cache_dict[(args, tuple(kwargs.items()))] = func(*args, **kwargs)
            return func(*args, **kwargs)
    return inner
