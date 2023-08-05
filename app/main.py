from typing import Callable


def cache(func: Callable) -> Callable:
    dict_of_args = {}

    def inner(*args, **kwargs) -> dict:
        if args not in dict_of_args.keys():
            dict_of_args[args] = func(*args)
            print("Calculating new result")
            return dict_of_args[args]
        else:
            print("Getting from cache")
            return dict_of_args[args]

    return inner
