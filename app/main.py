from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dictionary = {}

    def wrapper(*args, **kwargs) -> Any:
        args_key = (args, tuple(kwargs.items()))
        if args_key in cash_dictionary:
            print("Getting from cache")
            return cash_dictionary[args_key]
        else:
            result = func(*args, **kwargs)
            cash_dictionary[args_key] = result
            print("Calculating new result")
            return result
    return wrapper
