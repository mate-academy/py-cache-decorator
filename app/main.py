from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[key]

    return wrapper
