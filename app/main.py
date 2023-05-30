from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        key = args
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")

        results[key] = func(*args)
        return results[key]

    return wrapper
