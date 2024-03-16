from typing import Callable


def cache(func: Callable) -> Callable:

    results_dict = {}

    def wrapper(*args) -> None:
        func_args = args
        if func_args in results_dict:
            print("Getting from cache")
            return results_dict[func_args]

        else:
            results_dict[func_args] = func(*args)
            print("Calculating new result")
            return results_dict[func_args]
    return wrapper
1

