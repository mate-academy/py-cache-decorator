from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    args_dict = {}

    def saver(*args) -> Any:
        if args in args_dict:
            print("Getting from cache")
            return args_dict[args]
        else:
            args_dict[args] = func(*args)
            print("Calculating new result")
            return args_dict[args]
    return saver
