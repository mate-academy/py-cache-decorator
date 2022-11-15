from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_list = {}

    def wrapper(*args) -> Any:
        if args not in result_list:
            result_list[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result_list[args]
    return wrapper
