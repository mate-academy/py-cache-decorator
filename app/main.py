from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in results:
            print("Getting from cache")
            return results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result

        return result

    return wrapper


@cache
def long_time_func(
    first_number: int,
    second_number: int,
    third_number: int,
) -> int:
    return (
        first_number ** second_number + third_number
    ) % (first_number ** third_number)


@cache
def long_time_func_2(
    numbers_tuple: tuple[int, ...],
    power: int,
) -> list[int]:
    return [
        number ** power
        for number in numbers_tuple
    ]
