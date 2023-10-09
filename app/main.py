from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args) -> None:
        results = {}
        for arg in args:
            if arg in results:
                print("Getting from cache")
                print(results[arg])
            else:
                results.update({arg: func(*args)})
    return inner


@cache
def long_time_func(*args) -> None:
