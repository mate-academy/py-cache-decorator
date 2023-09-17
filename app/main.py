from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in result_cache:
            print("Getting from cache")
        else:
            result_cache[key] = func(*args, **kwargs)
            print("Calculating new result")

        return result_cache[key]

    return wrapper
