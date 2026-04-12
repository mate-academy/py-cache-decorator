from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        if args not in results:
            results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results[args]

    return wrapper
