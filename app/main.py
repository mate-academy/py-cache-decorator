from typing import Callable, Any


def cache(func: Callable) -> dict:
    list_of_results = {}

    def inner(*args: Any, **kwargs: Any) -> None:
        if args not in list_of_results:
            print("Calculating new result")
            list_of_results[args] = func(*args)
        else:
            print("Getting from cache")
        return list_of_results[args]
    return inner
