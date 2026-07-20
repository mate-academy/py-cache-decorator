from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper


@cache
def long_time_func(number: int, power: int, modulo: int) -> int:
    return (number ** power ** modulo) % (number * modulo)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list[int]:
    return [number ** power for number in numbers]
