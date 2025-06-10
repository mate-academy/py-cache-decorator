from typing import Callable


def cache(func: Callable) -> Callable:
    results_dict = {}

    def wrapper(*args):
        if args not in results_dict:
            print("Calculating new result")
            result = func(*args)
            results_dict[args] = result
            return result
        else:
            print("Getting from cache")
            return results_dict[args]
    return wrapper

