import functools
from typing import Callable, Any, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_data = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(numbers: Tuple[int], power: int) -> Tuple[int]:
    return tuple(number ** power for number in numbers)
