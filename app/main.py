from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cash:
            print("Getting from cache")
            return cash[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cash[args] = result
            return result

    return wrapper
