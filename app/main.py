from typing import Callable, Any


def cache(func: Callable) -> Callable:
    used = {}

    def inner(*args) -> Any:
        if args in used:
            print("Getting from cache")
            return used[args]

        else:
            print("Calculating new result")
            used[args] = func(*args)
            return used[args]
    return inner
