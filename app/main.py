from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def cache_checker(*args) -> Callable:
        if args in caches:
            print("Getting from cache")
        else:
            caches[args] = func(*args)
            print("Calculating new result")
        return caches[args]

    return cache_checker


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)
