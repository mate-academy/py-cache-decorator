from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args: Callable) -> Callable:
        if args not in result:
            func_result = func(*args)
            result.update({args: func_result})
            print("Calculating new result")
            return func_result
        else:
            print("Getting from cache")
            return result[args]

    return wrapper
