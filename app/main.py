from typing import Callable


def cache(func: Callable) -> Callable:
    dict_for_res = {}

    def inner(*args, **kwargs) -> tuple:
        if args in dict_for_res:
            print("Getting from cache")
        else:
            dict_for_res[args] = func(*args)
            print("Calculating new result")
        return dict_for_res[args]
    return inner
