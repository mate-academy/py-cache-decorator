from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dict = dict()

    def wrapper(*args: tuple) -> Any:

        if args in cash_dict:
            print("Getting from cache")
        else:
            cash_dict[args] = func(*args)
            print("Calculating new result")

        return cash_dict[args]
    return wrapper
