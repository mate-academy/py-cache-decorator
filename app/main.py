from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_items_and_results = {}

    @wraps(func)
    def inner(*args) -> Callable:

        if args in cash_items_and_results:
            print("Getting from cache")
        else:
            cash_items_and_results[args] = func(*args)
            print("Calculating new result")

        return cash_items_and_results[args]
    return inner
