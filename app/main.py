from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results.get(args)

        print("Calculating new result")
        results[args] = func(*args)
        return results.get(args)

    return inner
