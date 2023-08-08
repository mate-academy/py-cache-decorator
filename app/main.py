from typing import Callable, Any


def cache(func: Callable) -> dict:
    dict_results = {}

    def inner(*args) -> Any:
        result = None
        if args in dict_results:
            print("Getting from cache")
            result = dict_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
        dict_results.update({args: result})
        return result
    return inner
