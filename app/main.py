from typing import Callable


def cache(func: Callable) -> Callable:
    result_args_dict = {}

    def inner(*args) -> Callable:
        if args in result_args_dict:
            print("Getting from cache")
        else:
            result_args_dict[args] = func(*args)
            print("Calculating new result")
            return result_args_dict[args]
        return result_args_dict[args]
    return inner
