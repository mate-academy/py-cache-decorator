from typing import Callable, Any


def cache(func: Callable) -> Any:
    func_result = {}

    def wrapper(*args) -> Any:
        if args in func_result:
            print("Getting from cache")
        else:
            result = func(*args)
            func_result[args] = result
            print("Calculating new result")
        return func_result[args]

    return wrapper
