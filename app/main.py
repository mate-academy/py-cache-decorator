from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dictionary = {}

    def wrapper(*args, **kwargs) -> Any:
        args_key = (args, tuple(kwargs.items()))
        if args_key in cash_dictionary:
            print("Getting from cache")
        else:
            cash_dictionary[args_key] = func(*args, **kwargs)
            print("Calculating new result")
        return cash_dictionary[args_key]
    return wrapper
