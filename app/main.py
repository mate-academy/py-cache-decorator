import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args in func_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            func_dict[args] = func(*args)
        return func_dict[args]

    return wrapper
