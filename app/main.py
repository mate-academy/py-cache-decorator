from typing import Callable


def cache(func: Callable) -> Callable:
    stored_values = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in stored_values.keys():
            print("Getting from cache")
            return stored_values[args]
        else:
            print("Calculating new result")
            result_of_function = func(*args)
            stored_values[args] = result_of_function
            return result_of_function

    return wrapper
