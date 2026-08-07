from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args, **kwargs)

        return storage[args]

    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
