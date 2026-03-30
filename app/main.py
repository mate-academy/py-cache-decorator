from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args: tuple):
        if args in cache_memory:
            print("Getting from cache")
            return cache_memory[args]

        result = func(*args)
        cache_memory[args] = result
        print("Calculating new result")
        return result
    return inner

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




