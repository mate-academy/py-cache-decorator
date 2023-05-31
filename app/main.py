from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_storage = {}

    def wrapper(*args) -> Any:
        key_cash = args
        if key_cash not in cash_storage.keys():
            cash_storage[key_cash] = func(*args)
            print("Calculating new result")

            return cash_storage[key_cash]
        else:
            print("Getting from cache")

            return cash_storage[key_cash]

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
