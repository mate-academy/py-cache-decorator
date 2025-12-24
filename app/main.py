from typing import Callable


def cache(func: Callable) -> Callable:
    result_store = {}

    def wrapper(*args: any) -> any:
        if args in result_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_store[args] = func(*args)

        return result_store[args]

    return wrapper
