from typing import Callable


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def wrapper(*args: tuple) -> int:
        if args not in cash_dict:
            cash_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cash_dict[args]
    return wrapper
