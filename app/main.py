from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper
