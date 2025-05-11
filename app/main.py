from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    holder = {}

    @functools.wraps(func)
    def wrapper(*args) -> int:
        if args in holder:
            print("Getting from cache")
            return holder[args]
        print("Calculating new result")
        result = func(*args)
        holder[args] = result
        return result

    return wrapper
