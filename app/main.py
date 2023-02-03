from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Any:
        if args not in results:
            print("Calculating new result")
            results[args] = func(*args)
        else:
            print("Getting from cache")
        return results[args]

    return inner
