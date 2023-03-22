from typing import Any, Callable


def cache(func: Callable) -> Callable:
    stock = {}

    def wrapper(*args: Any) -> Any:
        if args in stock:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            stock[args] = result
        return stock[args]
    return wrapper
