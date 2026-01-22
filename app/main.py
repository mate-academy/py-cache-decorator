from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    args_dict = {}

    @wraps(func)
    def saver(*args) -> Any:
        if args in args_dict:
            print("Getting from cache")
            return args_dict[args]

        args_dict[args] = func(*args)
        print("Calculating new result")
        return args_dict[args]

    return saver
