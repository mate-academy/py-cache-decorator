from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper


@cache
def long_time_func(abetka: int, bukva: int, cukerka: int) -> int:
    return (abetka ** bukva ** cukerka) % (abetka * cukerka)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
