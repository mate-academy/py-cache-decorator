from typing import Callable

memory = {}


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> dict:
        key = args + tuple(kwargs.items()), func
        if key not in memory:
            memory[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return memory[key]

    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
