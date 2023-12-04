from typing import Callable


def cache(func: Callable) -> Callable:
    dict_ = {}

    def inner(*args) -> Callable:
        if args in dict_:
            print("Getting from cache")
            return dict_[args]
        else:
            result = func(*args)
            dict_[args] = result
            print("Calculating new result")
            return result
    return inner
