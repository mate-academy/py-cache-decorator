from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, depth: int) -> int:
    return (base ** exponent ** depth) % (base * depth)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list[int]:
    return [number ** power for number in numbers]
