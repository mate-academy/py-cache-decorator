from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = dict()

    def wrapper(*args) -> Callable:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            stored_results[args] = func(*args)
            print("Calculating new result")
            return stored_results[args]
    return wrapper
