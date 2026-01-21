from typing import Callable, List, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))
        if key in data:
            print("Getting from cache")
            return data[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            data[key] = res
            return res

    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[Any]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(1, 2, c=3)
