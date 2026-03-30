from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in data_cache:
            value = data_cache[key]
            print("Getting from cache")
        else:
            value = func(*args, **kwargs)
            print("Calculating new result")
            data_cache[key] = value
        return value
    return wrapper

# some commentar