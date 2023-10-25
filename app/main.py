from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args) -> int:
        func_name = func.__name__
        args_str = str(args)
        if func_name not in result_dict:
            result_dict[func_name] = {}
        if args_str not in result_dict[func_name]:
            result = func(*args)
            result_dict[func_name][args_str] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return result_dict[func_name][args_str]

    return inner
