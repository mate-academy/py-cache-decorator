from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in store:
            print("Getting from cache")
            return store[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result
    return wrapper
