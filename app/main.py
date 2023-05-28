from typing import Callable


def cache(func: Callable) -> Callable:
    results_dict = {}

    def inner(*args) -> int:
        if (*args,) in results_dict:
            print("Getting from cache")
        else:
            results_dict[(*args,)] = func(*args)
            print("Calculating new result")
        return results_dict[(*args,)]
    return inner
