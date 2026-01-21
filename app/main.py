from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args) -> int:
        if str(args) not in result_dict:
            result = func(*args)
            result_dict[str(args)] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return result_dict[str(args)]

    return inner
