from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_all = {}

    def inner(*args) -> Any:

        if args not in result_all:
            result_all[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result_all[args]

    return inner
