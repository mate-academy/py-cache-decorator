from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in cache_storage:
            print("Getting from cache")
            #print(args)
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            #print(result)
            return result

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


test1 = long_time_func(1, 2, 3)
test2 = long_time_func(2, 2, 3)
test3 = long_time_func_2((5, 6, 7), 5)
test4 = long_time_func(1, 2, 3)
test5 = long_time_func_2((5, 6, 7), 10)
test6 = long_time_func_2((5, 6, 7), 10)
