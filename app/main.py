from typing import Callable


def cache(func: Callable) -> Callable:
    result_store = {}

    def wrapper(*args: any) -> any:
        if args in result_store:
            print("Getting from cache")
            return result_store[args]
        else:
            print("Calculating new result")
            res = func(*args)
            result_store[args] = res
            return res

    return wrapper
