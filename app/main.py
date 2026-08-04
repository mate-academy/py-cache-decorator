from typing import Callable


def cache(func: Callable) -> Callable:
    saved = {}

    def wrapper(*args, **kwargs) -> None:
        if args in saved:
            print("Getting from cache")
            return saved[args]
        else:
            saved[args] = func(*args, **kwargs)
            print("Calculating new result")
            return saved[args]
    return wrapper


@cache
def long_time_func(a_arg: int, b_arg: int, c_arg: int) -> int:
    return (a_arg ** b_arg ** c_arg) % (a_arg * c_arg)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
