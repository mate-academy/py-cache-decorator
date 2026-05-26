from typing import Callable


def cache(func: Callable) -> Callable:
    from_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args not in from_cache:
            func_result = func(*args)
            print("Calculating new result")
            from_cache[args] = func_result
            return func_result
        else:
            print("Getting from cache")
            return from_cache[args]
    return wrapper
