from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored = {}

    def wrapper(*args) -> Any:
        if args in stored:
            print("Getting from cache")
            return stored[args]
        print("Calculating new result")
        result = func(*args)
        stored[args] = result
        return result

    return wrapper
