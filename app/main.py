from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def inner(*args) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        print("Calculating new result")
        saved_results[args] = func(*args)
        return saved_results[args]
    return inner
