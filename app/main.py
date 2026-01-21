from typing import Callable


def cache(func: Callable) -> Callable:
    results_dict = {}

    def wrapper(*args) -> Callable:
        if args in results_dict:
            print("Getting from cache")
            return results_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results_dict[args] = result
            return result

    return wrapper
