from functools import wraps
from typing import Callable, Any, Dict


def cache(func: Callable) -> Callable:
    storage: Dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, divisor: int) -> int:
    return (base ** exponent ** divisor) % (base * divisor)


@cache
def long_time_func_2(numbers_tuple: tuple, power: int) -> list:
    return [number ** power for number in numbers_tuple]


if __name__ == "__main__":
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)
