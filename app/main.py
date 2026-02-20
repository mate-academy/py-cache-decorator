from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = {}

    def wrapper(*args, **kwargs) -> None:
        current_key = args + tuple(sorted(kwargs.items()))
        if current_key in cache_list:
            print("Getting from cache")
            return cache_list[current_key]
        else:
            print("Calculating new result")
            cache_list[current_key] = func(*args, **kwargs)
            return cache_list[current_key]
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
