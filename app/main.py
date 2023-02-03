from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwargs) -> Any:
        if args not in results.keys():
            print("Calculating new result")
            results[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[args]

    return inner
