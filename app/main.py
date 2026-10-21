from typing import Any, Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        print("Calculating new result")
        result[args] = func(*args)
        return result[args]
    return wrapper
