from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:

        cache_key = (args, tuple(kwargs.items()))
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            return result
    return wrapper


@cache
def long_time_func(numer_one: int, numer_two: int, numer_three: int) -> int:
    return (numer_one ** numer_two ** numer_three) % (numer_one * numer_three)


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
