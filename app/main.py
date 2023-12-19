from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> Callable:

        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]
        else:
            result = func(*args, **kwargs)
            result_dict[args] = result
            print("Calculating new result")
            return result
    return inner
