from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))

        if key in store:
            print("Getting from cache")
            return store[key]

        result = func(*args, **kwargs)
        store[key] = result
        print("Calculating new result")
        return result

    return wrapper
