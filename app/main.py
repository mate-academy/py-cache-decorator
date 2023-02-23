from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_of_results = {}

    def inner(*args: Any, **kwargs: Any) -> Callable:
        if args not in dict_of_results:
            print("Calculating new result")
            dict_of_results[args] = func(*args)
        else:
            print("Getting from cache")
        return dict_of_results[args]
    return inner
