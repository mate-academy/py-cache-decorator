from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash = {}

    def init(*args) -> Any:
        if args in cash:
            print("Getting from cache")
            return cash[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cash[args] = res
            return res
    return init
