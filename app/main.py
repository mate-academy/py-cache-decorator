from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args) -> Any:
        if args in memo:
            print("Getting from cache")
            return memo[args]

        print("Calculating new result")
        result = func(*args)
        memo[args] = result
        return result

    return wrapper
