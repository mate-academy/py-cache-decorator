from typing import Callable


def cache(func: Callable) -> Callable:
    var_dict = {}
    def wrapper(*args, **kwargs) -> dict:
        key = (args, frozenset(kwargs.items()))
        if key in var_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            var_dict[key] = func(*args, **kwargs)
        return var_dict[key]
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

print(long_time_func(1, 2, 3))
print(long_time_func(2, 2, 3))
print(long_time_func_2((5, 6, 7), 5))
print(long_time_func(1, 2, 3))
print(long_time_func_2((5, 6, 7), 10))
print(long_time_func_2((5, 6, 7), 10))

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
