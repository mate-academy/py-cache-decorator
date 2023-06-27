from typing import Callable


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def function_cacher(*args) -> Callable:
        if args not in cash_dict:
            print("Calculating new result")
            cash_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return cash_dict[args]

    return function_cacher
