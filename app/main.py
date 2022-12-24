from typing import Callable


def cache(func: Callable) -> Callable:
    result_cash = {}

    def inner(*args) -> None:

        if args not in result_cash:
            print("Calculating new result")
            result_cash[args] = func(*args)
            return result_cash[args]

        print("Getting from cache")
        return result_cash[args]

    return inner
