from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args) -> any:
        res = data.get(args)
        if res is None:
            print("Calculating new result")
            res = func(*args)
            data[args] = res
        else:
            print("Getting from cache")
        return res

    return inner
