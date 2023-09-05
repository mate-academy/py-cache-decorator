from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    hash_table = {}

    def inner(*args: Any) -> None:
        key = str(args)
        if key in hash_table:
            print("Getting from cache")
        else:
            print("Calculating new result")
            hash_table[key] = func(*args)
        return hash_table[key]
    return inner


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func_2((5, 6, 7), 5)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
long_time_func_2([1, 2, 3], 10)
long_time_func_2([1, 2, 3], 10)
