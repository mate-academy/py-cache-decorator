from typing import Callable


def cache(func: Callable) -> Callable:
    cash_list = {}

    def inner(*args) -> int:
        if args in cash_list:
            print("Getting from cache")
            result = cash_list[args]
        else:
            result = func(*args)
            cash_list[args] = result
            print("Calculating new result")
        return result
    return inner
