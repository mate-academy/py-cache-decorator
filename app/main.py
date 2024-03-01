from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        result = cache_dict.get(key, None)

        if result is None:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")

        else:
            print("Getting from cache")

        return cache_dict[key]
    return wrapper
