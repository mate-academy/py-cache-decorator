from typing import Callable


def cache(func: Callable) -> Callable:
    store_result = {}

    def inner(*args) -> str:
        if args in store_result.keys():
            print("Getting from cache")
            return store_result[args]
        else:
            func_result = func(*args)
            store_result.update({args: func_result})
            print("Calculating new result")
            return func_result
    return inner
