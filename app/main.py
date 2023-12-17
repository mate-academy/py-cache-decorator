from typing import Callable


def cache(func: Callable) -> Callable:
    funcs = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key not in funcs:
            print("Calculating new result")
            result = func(*args, **kwargs)
            funcs[key] = result
        else:
            print("Getting from cache")
            result = funcs[key]
        return result

    return wrapper
