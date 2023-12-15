from typing import Callable


def cache(func: Callable) -> Callable:
    cash_list = {}

    def inner(*args) -> int:
        if str(args) in cash_list:
            print("Getting from cache")
            return cash_list[str(args)]
        else:
            result = func(*args)
            cash_list[str(args)] = result
            print("Calculating new result")
            return result
    return inner
