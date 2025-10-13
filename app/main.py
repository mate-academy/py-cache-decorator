from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage.get(key)
        else:
            print("Calculating new result")
            new_result = func(*args, **kwargs)
            cache_storage[key] = new_result
            return new_result
    return wrapper


@cache
def long_time_func(base: int, exponent: int, mod_base: int) -> int:
    return (base ** exponent ** mod_base) % (base * mod_base)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]

