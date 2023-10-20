from typing import Callable


def cache(func: Callable) -> Callable:
    completed_runs = {}

    def wrapper(*args) -> list:

        if args in completed_runs:
            print("Getting from cache")
        else:
            print("Calculating new result")
            completed_runs.update({args: func(*args)})

        return completed_runs[args]

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
