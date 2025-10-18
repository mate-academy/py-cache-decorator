from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))
        if key not in results:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[key]

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulo_base: int) -> int:
    return (base ** exponent ** modulo_base) % (base * modulo_base)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list[int]:
    return [number ** power for number in numbers]
