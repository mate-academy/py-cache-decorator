from typing import Any, Callable


def cache(func: Callable) -> Callable:
    agrums_and_results_dict = {}

    def wpapper_func(*args) -> Any:
        if args in agrums_and_results_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            agrums_and_results_dict[args] = func(*args)
        return agrums_and_results_dict[args]
    return wpapper_func
