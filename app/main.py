from typing import Callable


def cache(func: Callable) -> None:
    my_cash = {}

    def inner(*args) -> str:
        if args not in my_cash.keys():
            my_cash[args] = func(*args)
            print("Calculating new result")
            return my_cash[args]
        else:
            print("Getting from cache")
            return my_cash[args]

    return inner

