from typing import Callable


def cache(func: Callable) -> Callable:
    dict_with_arguments = {}

    def inner(*args) -> int:
        if args in dict_with_arguments:
            print("Getting from cache")
            return dict_with_arguments[args]
        print("Calculating new result")
        saved_result = func(*args)
        dict_with_arguments[args] = saved_result
        return saved_result
    return inner
