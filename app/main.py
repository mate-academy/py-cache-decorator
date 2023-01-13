from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = dict()

    def inner(*args: Any) -> Any:

        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            results[args] = func(*args)
            print("Calculating new result")
            return results[args]
    return inner
