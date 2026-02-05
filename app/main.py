from typing import Callable


def cache(func: Callable) -> Callable:
    vault = {}

    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in vault:
            print("Getting from cache")
            return vault[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            vault[key] = result
            return result
    return wrapper
