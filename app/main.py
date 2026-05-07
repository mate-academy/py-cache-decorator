from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

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
def long_time_func(arg1: int, arg2: int, arg3: int) -> int:
    return (arg1 ** arg2 ** arg3) % (arg1 * arg3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
