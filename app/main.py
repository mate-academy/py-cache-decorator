from typing import Callable, Any


def cache(func: Callable) -> Callable:
    res = {}

    def inner(*args: tuple, **kwargs: dict) -> Any:
        if args in res:
            print("Getting from cache")
            return res[args]
        res[args] = func(*args)
        print("Calculating new result")
        return res[args]

    return inner
