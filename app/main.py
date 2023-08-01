from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Any:
        if args not in results:
            print("Calculating new result")
            value = func(*args)
            results[args] = value
            return value
        else:
            print("Getting from cache")
            return results[args]
    return inner
