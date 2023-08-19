from typing import Callable


def cache(func: Callable) -> Callable:
    dict_res = {}

    def inner(*args) -> Callable:
        if args not in dict_res:
            result_func = func(*args)
            dict_res[args] = result_func
            print("Calculating new result")
        else:
            print("Getting from cache")
        return dict_res[args]
    return inner
