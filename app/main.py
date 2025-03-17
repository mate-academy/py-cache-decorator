from typing import Callable

def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        nonlocal var_dict
        key = (args, frozenset(kwargs.items()))
        if key in var_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            var_dict[key] = func(*args, **kwargs)
        return var_dict[key]
    var_dict = {}
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))  # "Calculating new result"
print(long_time_func(2, 2, 3))  # "Calculating new result"
print(long_time_func_2((5, 6, 7), 5))  # "Calculating new result"
print(long_time_func(1, 2, 3))  # "Getting from cache"
print(long_time_func_2((5, 6, 7), 10))  # "Calculating new result"
print(long_time_func_2((5, 6, 7), 10))  # "Getting from cache"
