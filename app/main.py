from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    stored_caches = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        for item_args in args:
            if isinstance(item_args, (set, list, dict)):
                return func(*args, **kwargs)
        for item_kwargs in kwargs.values():
            if isinstance(item_kwargs, (set, list, dict)):
                return func(*args, **kwargs)
        if ((args, tuple(sorted(kwargs.items())),
            func)
                in stored_caches):
            print("Getting from cache")
            return stored_caches[(args,
                                  tuple(sorted(kwargs.items())),
                                  func)]
        print("Calculating new result")
        rez = func(*args, **kwargs)
        stored_caches[(args,
                       tuple(sorted(kwargs.items())), func)] = rez
        return rez
    return wrapper


@cache
def long_time_func(var_a: int, var_b: int, var_c: int) -> int:
    return (var_a ** var_b ** var_c) % (var_a * var_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
