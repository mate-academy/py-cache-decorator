from typing import Callable


def cache(func: Callable) -> Callable:
    cash_items_and_results = {}

    def inner(*args) -> Callable:

        if args in cash_items_and_results:
            print("Getting from cache")
            return cash_items_and_results[args]

        else:
            cash_items_and_results[args] = func(*args)
            print("Calculating new result")

            return cash_items_and_results[args]

    return inner
