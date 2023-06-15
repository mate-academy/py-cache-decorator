from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def function_cacher(*args) -> Any:
        nonlocal cash_dict
        key = str(args)
        if key not in cash_dict:
            print("Calculating new result")
            cash_dict[key] = func(*args)
        else:
            print("Getting from cache")
        return cash_dict[key]

    return function_cacher
