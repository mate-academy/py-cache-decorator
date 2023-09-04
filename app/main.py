from typing import Callable


def cache(func: Callable) -> Callable:
    list_of_args = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in list_of_args.keys():
            list_of_args[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return list_of_args[args]
    return inner
