from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    Decorator that caches the results of function calls.
    """
    cache_storage = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[args] = result
            return result

    return wrapper


# --- Testy ---
@cache
def long_time_func(base: int, exponent: int, sub_exponent: int) -> int:
    return (base ** exponent ** sub_exponent) % (base * sub_exponent)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return tuple(number ** power for number in n_tuple)


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
