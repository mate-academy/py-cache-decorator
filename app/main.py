from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> None:
        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args, **kwargs)
            print("Calculating new result")
        return result[args]
    return inner
