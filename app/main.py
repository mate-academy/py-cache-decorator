from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args: Any) -> Any:
        if args not in cached:
            print("Calculating new result")
            result = func(*args)
            cached[args] = func(*args)
            return result

        print("Getting from cache")
        return cached[args]

    return inner
