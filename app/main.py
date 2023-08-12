from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args) -> Any:
        if args in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[args] = func(*args)
        return result_dict[args]

    return wrapper
