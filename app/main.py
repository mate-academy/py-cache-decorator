from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dic = dict()

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        key_cach = ", ".join([func.__name__, str(args), str(kwargs)])

        if key_cach in cache_dic:
            print("Getting from cache")
            return cache_dic[key_cach]

        cache_dic[key_cach] = func(*args, **kwargs)

        print("Calculating new result")
        return cache_dic[key_cach]

    return inner


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


@cache
def long_time_func(num: int, num2: int, num3: int) -> int:
    return (num ** num2 ** num3) % (num * num3)


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
