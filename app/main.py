from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        # Повертаємо результат в одному місці для обох випадків
        return cache_dict[key]

    return wrapper


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
