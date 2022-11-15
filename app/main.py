import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    args_results = {}

    @functools.wraps(func)
    def inner(*args) -> Callable:
        if args not in args_results:
            print("Calculating new result")
            result = func(*args)
            args_results[args] = result
        else:
            print("Getting from cache")
        return args_results[args]
    return inner


@cache
def long_time_func(alfa: int, beta: int, ceta: int) -> int:
    return (alfa ** beta ** ceta) % (alfa * ceta)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))
print(long_time_func(2, 2, 3))
print(long_time_func_2((5, 6, 7), 5))
print(long_time_func(1, 2, 3))
print(long_time_func_2((5, 6, 7), 10))
print(long_time_func_2((5, 6, 7), 10))
