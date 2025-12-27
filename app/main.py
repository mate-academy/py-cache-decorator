from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_data:
            print("Getting from cache")
            return cached_data[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data[key] = result
            return result

    return inner
