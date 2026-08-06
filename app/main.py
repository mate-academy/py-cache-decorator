from typing import Any, Callable


def cache(func: Callable) -> Callable:
    func._cache = {}

    def inner(*args) -> Any:
        if args not in func._cache:
            func._cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return func._cache[args]

    return inner