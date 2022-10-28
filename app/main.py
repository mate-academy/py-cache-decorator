from typing import Callable


def cache(func: Callable) -> Callable:
    func_arg_res = {}

    def inner(*args, **kwargs) -> Callable:
        if f"{args},{kwargs}" not in func_arg_res:
            func_result = func(*args, **kwargs)
            func_arg_res[f"{args},{kwargs}"] = func_result
            print("Calculating new result")
            return func_result
        else:
            print("Getting from cache")
            return func_arg_res[f"{args},{kwargs}"]

    return inner
