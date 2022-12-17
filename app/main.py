from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def init(*args) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]
        print("Calculating new result")
        res = func(*args)
        data[args] = res
        return res
    return init
