from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args: object) -> object:
        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]

        else:
            print("Calculating new result")
            res = func(*args)
            result_dict[args] = res

            return res

    return wrapper
