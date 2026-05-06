from typing import Any, Callable


def cache(func: Callable) -> Callable:
    our_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in our_cache:
            print("Getting from cache")
            return our_cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        our_cache[key] = result
        return result

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]
