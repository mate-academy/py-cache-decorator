from typing import Callable, Any


def cache(func: Callable) -> Callable:
    list_of_arguments_and_rsults = {}

    def wrapper(*args) -> Any:
        if args not in list_of_arguments_and_rsults:
            result = func(*args)
            list_of_arguments_and_rsults[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return list_of_arguments_and_rsults[args]
    return wrapper
