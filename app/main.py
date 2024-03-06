from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> any:
        if args not in saved_results:
            print("Calculating new result")
            saved_results[args] = func(*args)
        else:
            print("Getting from cache")
        return saved_results[args]
    return wrapper
