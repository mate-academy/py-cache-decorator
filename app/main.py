from typing import Callable


def cache(func: Callable) -> Callable:
    data_dict = {}

    def inner(*args: tuple) -> int:
        if args in data_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data_dict[args] = func(*args)
        return data_dict[args]
    return inner
