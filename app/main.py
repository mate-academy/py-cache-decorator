from typing import Callable

def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args):
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int):
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
