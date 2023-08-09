from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = dict()

    def wrapped(*args) -> Any:
        if args in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[args] = func(*args)

        return cached[args]

    return wrapped
