from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> Callable:

        if (args or kwargs) in result:
            print("Getting from cache")

        else:
            print("Calculating new result")
            result[(args or kwargs)] = func(*args, **kwargs)
        return result[(args or kwargs)]

    return inner
