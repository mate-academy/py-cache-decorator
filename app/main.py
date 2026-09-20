from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> object:
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)
        return results[args]

    return wrapper
