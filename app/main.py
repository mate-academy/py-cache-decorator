from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> dict:
        key = str(args) + str(kwargs)
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            result[key] = res
            return res

    return inner
