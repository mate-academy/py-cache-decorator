from typing import Callable


def cache(func: Callable) -> Callable:

    result: dict = {}

    def inner(*args) -> None:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            res = func(*args)
            result[args] = res
            return res
    return inner
