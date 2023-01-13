from typing import Callable


def cache(func: Callable, *args, **kwargs) -> Callable:
    cache_dict = {}

    def wrapper(*spisok) -> Callable:
        if spisok in cache_dict:
            print("Getting from cache")
            return cache_dict.get(spisok)
        else:
            print("Calculating new result")
            result = func(*spisok)
            cache_dict[spisok] = result
            return result
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
