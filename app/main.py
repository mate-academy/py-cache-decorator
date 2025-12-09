from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cache_memory:
            print("Getting from cache")
            return cache_memory[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_memory[key] = result
        return result
    return wrapper


@cache
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[int]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
