from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> int:

        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        result = func(*args, **kwargs)
        cache_dict[args] = result
        print("Calculating new result")
        return result

    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
