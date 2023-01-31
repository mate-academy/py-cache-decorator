from typing import Callable, Any


def cache(func: Callable) -> Any:
    func_result = {}

    def wrapper(*args) -> Any:
        if args in func_result.keys():
            print("Getting from cache")
            return func_result[args]
        else:
            res = func(*args)
            func_result[args] = res
            print("Calculating new result")
            return res

    return wrapper
