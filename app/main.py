from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args: any) -> any:
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        results.update({args: func(*args)})
        return results[args]

    return inner
