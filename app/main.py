from typing import Callable


def cache(func: Callable) -> None:
    results = {}

    def inner(*args) -> Callable:
        if args in results:
            print("Getting from cache")
            return results[args]

        not_repeat = func(*args)
        results[args] = not_repeat
        print("Calculating new result")
        return not_repeat

    return inner
