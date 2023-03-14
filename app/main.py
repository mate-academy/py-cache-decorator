from typing import Callable


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args) -> dict:
        if args in memo:
            print("Getting from cache")
            return memo[args]
        else:
            print("Calculating new result")
            new_value = func(*args)
            memo[args] = new_value
            return new_value

    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
