from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}
    def wrapper (*args, **kwargs):
        args_key = tuple(args) + tuple(sorted(kwargs.items()))
        if args_key in func_cache:
            print("Getting from cache")
            return func_cache[args_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[args_key] = result
            return result
    return wrapper


