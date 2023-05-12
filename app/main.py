from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cash_results_per_function = {}

    def inner(*args) -> Callable:

        if args in stored_cash_results_per_function:
            print("Getting from cache")
            return stored_cash_results_per_function[args]

        else:
            stored_cash_results_per_function[args] = func(*args)
            print("Calculating new result")

            return stored_cash_results_per_function[args]

    return inner
