from typing import Callable


def cache(func: Callable) -> None:

    new_dict = {}

    def inner(*args) -> str:
        if args not in new_dict.keys():
            new_dict[args] = func(*args)
            print("Calculating new result")
            return new_dict[args]
        else:
            print("Getting from cache")
            return new_dict[args]

    return inner
