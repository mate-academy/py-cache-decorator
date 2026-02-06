from typing import Callable


def cache(func: Callable) -> Callable:
    trash = {}

    def inner(*args, **kwargs) -> object:
        key = (args, tuple(kwargs.items()))
        if key in trash:
            print("Getting from cache")
            return trash[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            trash[key] = res
            return res
    return inner
