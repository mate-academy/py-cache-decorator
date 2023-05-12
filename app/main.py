from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_cash_results_per_function = {}

    @wraps(func)
    def inner(*args) -> Callable:

        if args in stored_cash_results_per_function:
            print("Getting from cache")
        else:
            stored_cash_results_per_function[args] = func(*args)
            print("Calculating new result")

        return stored_cash_results_per_function[args]

    return inner
