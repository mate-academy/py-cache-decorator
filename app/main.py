from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}
    def inner(*args):
        if args in memory.keys():
            print("Getting from cache")
            print(memory[args])
            return memory[args]
        else:
            print("Calculating new result")
            t = func(*args)
            memory[args] = t
            print(t)
            return t
    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func(1, 2, 3)
long_time_func(3, 4, 5)
long_time_func(3, 4, 5)
long_time_func_2((1, 2, 3), 5)
long_time_func_2((4, 5, 6), 5)
long_time_func_2((1, 2, 3), 5)