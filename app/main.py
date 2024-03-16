from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    results_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> None:
        func_args = args
        if func_args in results_dict:
            print("Getting from cache")
            return results_dict[func_args]

        results_dict[func_args] = func(*args)
        print("Calculating new result")
        return results_dict[func_args]
    return wrapper
