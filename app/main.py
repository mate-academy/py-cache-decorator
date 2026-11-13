from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper


@cache
def long_time_func(first_number: int, second_number: int, third_number: int)\
        -> int:
    return ((first_number ** second_number ** third_number) %
            (first_number * third_number))


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
