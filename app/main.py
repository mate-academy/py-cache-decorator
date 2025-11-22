from typing import Callable
from typing import Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[int]:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))  # Calculating new result
print(long_time_func(2, 2, 3))  # Calculating new result
print(long_time_func_2((5, 6, 7), 5))  # Calculating new result
print(long_time_func(1, 2, 3))  # Getting from cache
print(long_time_func_2((5, 6, 7), 10))  # Calculating new result
print(long_time_func_2((5, 6, 7), 10))  # Getting from cache
