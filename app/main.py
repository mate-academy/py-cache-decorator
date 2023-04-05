from typing import Any, Callable


def cache(func: Callable) -> Callable:

    results_dict = {}

    def inner(*args: tuple) -> Any:
        if args not in results_dict.keys():
            print("Calculating new result")
            results_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return results_dict[args]
    return inner
