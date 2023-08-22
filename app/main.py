from typing import Callable


def cache(func: Callable) -> Callable:
    dict_of_args = {}

    def inner(*args) -> dict:
        if args not in dict_of_args:
            dict_of_args[args] = func(*args)
            print("Calculating new result")
            return dict_of_args[args]
        print("Getting from cache")
        return dict_of_args[args]

    return inner
