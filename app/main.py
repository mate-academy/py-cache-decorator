from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwargs) -> Callable:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        results[args] = func(*args, **kwargs)
        return results[args]
    return inner
