from typing import Callable


def cache(func: Callable) -> Callable:
    cash = {}

    def inner(*args) -> int:
        if cash.get(f"({func},{args})") is None:
            result = func(*args)
            cash[f"({func},{args})"] = result
            print("Calculating new result")
            return result

        print("Getting from cache")
        return cash.get(f"({func},{args})")

    return inner
