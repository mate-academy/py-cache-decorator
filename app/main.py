from typing import Callable

def cache(func: Callable) -> Callable:
    dict_of_args = {}

    def inner(*args) -> Callable:
        if args in dict_of_args.keys():
            print("Getting from cache")
        else:
            dict_of_args[args] = func(*args)
            print("Calculating new result")
        return dict_of_args[args]
    return inner

