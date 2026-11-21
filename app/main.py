from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))  # create a key here
        if key in results:
            print("Getting from cache")
            return results[key]   # check results
        else:
            print("Calculating new result")
        results[key] = func(*args, **kwargs)
        return results[key]    # calculate and save if needed
    return wrapper


@cache
def long_time_func(a1: int, b1: int, c1: int) -> int:
    return (a1 ** b1 ** c1) % (a1 * c1)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
