from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> None:
        nonlocal results
        if args in results:
            print("Getting from cache")
            print(results[args])
        else:
            print("Calculating new result")
            results.update({args: func(*args)})
    return inner


@cache
def do_something(*args) -> None:
