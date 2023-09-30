from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper


@cache
def long_time_func(arg1: int, arg2: int, arg3: int) -> int:
    return (arg1 ** arg2 ** arg3) % (arg1 * arg3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
