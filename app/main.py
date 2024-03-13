from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_result = {}

    def wrapper(*args) -> Any:
        cash_key = tuple(args)
        if cash_key in cash_result:
            print("Getting from cache")
            return cash_result[cash_key]

        result = func(*args)
        cash_result[cash_key] = result
        print("Calculating new result")
        return result

    return wrapper
