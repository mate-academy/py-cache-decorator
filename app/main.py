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
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


long_time_func(1, 2, 3)
long_time_func(1, 2, 3.2)
long_time_func(1, 2, 3)
