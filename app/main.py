from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> dict:
        args_tuple = args + tuple(kwargs.items())
        if args_tuple in results_cache:
            print("Getting from cache")
        else:
            results_cache[args_tuple] = func(*args, **kwargs)
            print("Calculating new result")
        return results_cache[args_tuple]

    return wrapper


@cache
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[Any]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
