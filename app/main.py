from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dic_args = {}

    def wrapper(*args) -> Any:
        if args in result_dic_args:
            print("Getting from cache")
            return result_dic_args[args]
        else:
            print("Calculating new result")
            result = func(*args)
            result_dic_args[args] = result
            return result
    return wrapper
