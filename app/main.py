from typing import Callable, Any


def cache(func: Callable) -> Callable:
    database = {}

    def inner(*args) -> Any:
        if args in database:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            database[args] = result
        return database[args]

    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]



