from typing import Callable, Any


def cache(func: Callable) -> Any:
    result_dict = {}

    def inner(*args) -> Any:
        if args not in result_dict:
            print("Calculating new result")
            result_dict[args] = func(*args)
            return result_dict[args]
        else:
            print("Getting from cache")
            return result_dict[args]
    return inner
