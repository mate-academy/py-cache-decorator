from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    result = dict()

    def inner(*args) -> Any:
        if args not in result:
            print("Calculating new result")
            result[args] = func(*args)
            return result[args]
        else:
            print("Getting from cache")
            return result[args]
    return inner
