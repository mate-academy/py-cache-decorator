from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> Callable:

        if args in result_dict:
            print("Getting from cache")
        else:
            result_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
        return result_dict[args]
    return inner
