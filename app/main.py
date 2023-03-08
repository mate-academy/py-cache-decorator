from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = dict()

    def inner(*args) -> Any:
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        results[args] = func(*args)
        return results[args]
    return inner
