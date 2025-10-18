from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args: any, **kwargs: any) -> any:
        key = (args, tuple(kwargs.items()))
        if key not in results:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[key]
    return wrapper
@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

