from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args: None) -> None:
        if args in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args)
        return cache_data[args]
    return wrapper


@cache
def long_time_func(aaa: int, bbb: int, ccc: int) -> int:
    return (aaa ** bbb ** ccc) % (aaa * ccc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
