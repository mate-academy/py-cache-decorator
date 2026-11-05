from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = dict()

    def inner(*args) -> int:
        key = args, func.__name__
        if key not in saved_results:
            saved_results[key] = func(*args)
            print("Calculating new result")
            return saved_results[key]
        else:
            print("Getting from cache")
            return saved_results[key]
    return inner
