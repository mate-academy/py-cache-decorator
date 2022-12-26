from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> int:
        nonlocal results
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            result = func(*args)
            results[args] = result
            print("Calculating new result")
            return result
    return inner
