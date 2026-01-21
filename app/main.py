from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> dict:

        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        result = func(*args)
        results[args] = result
        return result

    return inner


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
