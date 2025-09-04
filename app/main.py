from typing import Callable, Any


def cache(func: Callable) -> Callable:
    calculated = dict()
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in calculated:
            print("Getting from cache")
            return calculated.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            calculated[key] = result
            return result
    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

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
