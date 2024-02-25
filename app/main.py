from typing import Callable
import functools


cached = {}


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args) -> int:
        global cached
        key = str(id(func)) + "(" + f"{args}" + ")"
        # print(key)
        if key not in cached:
            print("Calculating new result")
            result = func(*args)
            cached[key] = result
        else:
            print("Getting from cache")
            result = cached[key]
        return result
    return wrapper
