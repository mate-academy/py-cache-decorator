from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwarg) -> float:
        if args not in results:
            print("Calculating new result")
            results[args] = func(*args)
            return results[args]
        else:
            print("Getting from cache")
            return results[args]
    return inner
