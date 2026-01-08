from functools import wraps
from typing import Callable, Iterable


def make_hashable_key(*args, **kwargs) -> tuple:
    def convert_to_hashable(obj: Iterable) -> tuple:
        if isinstance(obj, dict):
            return tuple(sorted((k, convert_to_hashable(v))
                                for k, v in obj.items()))
        elif isinstance(obj, list):
            return tuple(convert_to_hashable(item) for item in obj)
        elif isinstance(obj, set):
            return tuple(sorted(convert_to_hashable(item) for item in obj))
        elif isinstance(obj, tuple):
            return tuple(convert_to_hashable(item) for item in obj)
        else:
            return obj

    hashable_args = tuple(convert_to_hashable(arg) for arg in args)
    hashable_kwargs = tuple(sorted((k, convert_to_hashable(v))
                                   for k, v in kwargs.items()))
    return (hashable_args, hashable_kwargs)


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = make_hashable_key(*args, **kwargs)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper


@cache
def long_time_func(vara: int, varb: int, varc: int) -> int:
    return (vara ** varb ** varc) % (vara * varc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":

    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2([5, 6, 7], 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
