from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cashed_data = {}

    def inner_function(*args) -> Any:
        if args in cashed_data:
            print("Getting from cache")
            return cashed_data[args]
        else:
            print("Calculating new result")
            func_returned_value = func(*args)
            cashed_data[args] = func_returned_value
            return func_returned_value
    return inner_function
