from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    def inner(*args, **kwargs) -> dict:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            print("Calculating new result")
            stored_results[args] = func(*args, **kwargs)
            return stored_results[args]
    return inner
