from typing import Callable, Any
from functools import wraps
cache_dic = dict()


def cache(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key_cache = func.__name__ + str(args) + str(kwargs)

        if key_cache in cache_dic:
            print("Getting from cache")
            return cache_dic[key_cache]

        cache_dic[key_cache] = func(*args, **kwargs)

        print("Calculating new result")
        return cache_dic[key_cache]

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
