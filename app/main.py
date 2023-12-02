from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")
            return result

    return wrapper


@cache
def long_time_func(abetka: int, bukva: int, cukerka: int) -> int:
    return (abetka ** bukva ** cukerka) % (abetka * cukerka)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
