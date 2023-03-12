from typing import Any, Callable


def cache(func: Callable) -> Any:
    sum_cache = {}

    def wrapped(*args: Callable) -> Any:
        if args not in sum_cache:
            temp_cache = func(*args)
            sum_cache[args] = temp_cache
            print("Calculating new result")
            return temp_cache
        else:
            print("Getting from cache")
            return sum_cache[args]

    return wrapped
