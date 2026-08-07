from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:

        if args not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args] = result
        else:
            print("Getting from cache")
            return cache_dict[args]

        return result

    return wrapper


@cache
def long_time_func(number1: int, number2: int, number3: int) -> int:
    return (number1 ** number2 ** number3) % (number1 * number3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
