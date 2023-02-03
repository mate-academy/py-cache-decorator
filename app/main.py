from typing import Callable


def cache(func: Callable) -> Callable:
    data_dict = {}

    def inner(*args: Callable) -> Callable:

        if args in data_dict:
            print("Getting from cache")
            return data_dict[args]
        else:
            print("Calculating new result")
            value_for_arg = func(*args)
            data_dict[args] = value_for_arg
            return value_for_arg
    return inner
