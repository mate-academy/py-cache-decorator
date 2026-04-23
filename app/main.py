from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result
    return wrapper


@cache
def long_time_func(a_num: int, b_num: int, c_num: int) -> int:
    return (a_num ** b_num ** c_num) % (a_num * c_num)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
