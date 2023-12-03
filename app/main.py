from typing import Callable


def cache(func: Callable) -> Callable:
    store_results = {}

    def inner(*args) -> str:
        if args in store_results.keys():
            print("Getting from cache")
            return store_results[args]
        else:
            func_result = func(*args)
            store_results.update({args: func_result})
            print("Calculating new result")
            return func_result
    return inner
