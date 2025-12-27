from typing import Callable


def cache(func: Callable) -> Callable:
    cash_storeg = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple((kwargs.items())))
        if key in cash_storeg:
            print("Getting from cache")
            return cash_storeg[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cash_storeg[key] = result
        return result
    return wrapper
