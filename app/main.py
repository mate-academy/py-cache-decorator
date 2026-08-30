

from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Getting from cache")
            result = cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper


@cache
def long_time_func(int1: int, int2: int, int3: int) -> int:
    return (int1 ** int2 ** int3) % (int1 * int3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
