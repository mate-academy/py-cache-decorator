from typing import Callable
import functools


immutable_types = (int, float, complex, bool, str,
                   tuple, frozenset, bytes, type(None))


def check_immutable_args(*args, **kwargs) -> None:
    all_values = list(args) + list(kwargs.values())
    for value in all_values:
        if not isinstance(value, immutable_types):
            raise TypeError(
                f"Аргумент {value!r} має тип {type(value).__name__}, "
                f"який є mutable. Функції, декоровані @cache, "
                f"повинні приймати лише immutable аргументи."
            )


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        check_immutable_args(*args, **kwargs)
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result
        return result
    return wrapper
