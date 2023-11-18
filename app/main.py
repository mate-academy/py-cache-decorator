from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_func_names = []
    cached_func_args = []
    cached_func_res = []

    @wraps(func)
    def wrapper(*args) -> int:
        func_name = func.__name__
        for i in range(len(cached_func_names)):
            if func_name == cached_func_names[i]:
                if args == cached_func_args[i]:
                    print("Getting from cache")
                    return cached_func_res[i]

        print("Calculating new result")
        res = func(*args)
        cached_func_names.append(func_name)
        cached_func_args.append(args)
        cached_func_res.append(res)

        return res

    return wrapper
