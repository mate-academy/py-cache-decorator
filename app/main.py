from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwargs) -> int:
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args, **kwargs)
        return results[args]
    return inner
