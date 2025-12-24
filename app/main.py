from typing import Callable, Any


def cache(func: Callable) -> Callable:

    result = {}

    def inner(*args) -> Any:
        if str(args) in result.keys():
            print("Getting from cache")
        else:
            result[str(args)] = func(*args)
            print("Calculating new result")
        return result[str(args)]

    return inner
