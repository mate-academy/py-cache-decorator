from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored = dict()

    def wrapper(*args) -> Any:
        if func not in stored:
            stored[func] = dict()
        if args not in stored[func]:
            print("Calculating new result")
            result = func(*args)
            stored[func][args] = result
            return result
        else:
            print("Getting from cache")
            return stored[func][args]

    return wrapper
