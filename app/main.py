from typing import Callable


def cache(func: Callable) -> Callable:
    store_results = {}

    def inner(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key not in store_results:
            store_results[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return store_results[key]

    return inner
