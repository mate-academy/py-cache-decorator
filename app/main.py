from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cash = {}

    def wrapper(*args) -> str:
        key = (func, args)
        if key in dict_cash:
            print("Getting from cache")
            return dict_cash[key]
        else:
            print("Calculating new result")
            new_cash = func(*args)
            dict_cash[key] = new_cash
            return new_cash
    return wrapper
