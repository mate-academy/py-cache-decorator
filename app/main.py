from typing import Callable


def cache(func: Callable) -> Callable:
    result_args_dict = {}

    def inner(*args) -> None:
        if args in result_args_dict:
            print("Getting from cache")
            return result_args_dict[args]
        else:
            value = func(*args)
            result_args_dict[args] = value
            print("Calculating new result")
            return value
    return inner
