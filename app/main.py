from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        key = args

        if key in results.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args)

        return results[key]
    return wrapper
