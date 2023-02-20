from typing import Callable, Any


def cache(func: Callable) -> None:
    list_of_results = {}

    def inner(*args: Any, **kwargs: Any) -> None:
        if isinstance(args, (int, str, float, bool, tuple)):
            if args not in list_of_results:
                print("Calculating new result")
                list_of_results[args] = func(*args)
                return list_of_results[args]
            print("Getting from cache")
            return list_of_results[args]
    return inner
