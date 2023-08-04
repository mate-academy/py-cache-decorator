from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Callable:
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result
    return inner
