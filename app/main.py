from typing import Callable


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def function_cacher(*args, **kwargs) -> Callable:
        nonlocal cash_dict
        args_kvargs_key = f"{args} {kwargs}"
        if args_kvargs_key not in cash_dict:
            print("Calculating new result")
            cash_dict[args_kvargs_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cash_dict[args_kvargs_key]

    return function_cacher
