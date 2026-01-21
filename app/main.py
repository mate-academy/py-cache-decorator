from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        result = cache_dict.get(key, None)

        if result is not None:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper
