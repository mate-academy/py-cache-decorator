from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwargs) -> Callable:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        results[args] = func(*args, **kwargs)
        return results[args]
    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple[int], power: int) -> list[int]:
    return [number ** power for number in n_tuple]
