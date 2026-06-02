from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        print("Calculating new result")
        res = func(*args)
        result[args] = res
        return res
    return inner
