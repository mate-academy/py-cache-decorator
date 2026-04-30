from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        if (args, tuple((kwargs.items()))) in cache_dict:
            print("Getting from cache")
            return cache_dict[(args, tuple((kwargs.items())))]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[(args, tuple((kwargs.items())))] = result
            return result
    return wrapper
