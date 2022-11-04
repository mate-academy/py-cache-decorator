from typing import Callable


def cache(func: Callable) -> Callable:
    func_arg_res = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in func_arg_res:
            func_result = func(*args, **kwargs)
            func_arg_res[args] = func_result
            print("Calculating new result")
            return func_result
        else:
            print("Getting from cache")
            return func_arg_res[args]

    return inner
