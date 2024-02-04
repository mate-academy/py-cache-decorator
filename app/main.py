from typing import Callable


def cache(func: Callable) -> Callable:
    cash = {}

    def wrapper(*args, **kwargs) -> int:
        for item in cash:
            if f"{func}, {args}" in cash:
                print("Getting from cache")
                return cash[f"{func}, {args}"]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cash[f"{func}, {args}"] = result
            return result
    return wrapper
