from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args) -> int:
        cash_list = getattr(inner, "cash_list", {})

        if str(args) in cash_list:
            print("Getting from cache")
            return cash_list[str(args)]
        else:
            result = func(*args)
            cash_list[str(args)] = result
            print("Calculating new result")

            inner.cash_list = cash_list

            return result

    return inner
