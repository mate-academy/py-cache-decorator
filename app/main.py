from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def wrapper(*args: Any) -> Any:
        if args in cash_dict:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cash_dict[args] = func(*args)
        return cash_dict[args]

    return wrapper
