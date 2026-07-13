from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            return result
    return wrapper


@cache
def long_time_func(number_one: int, number_two: int, number_three: int) -> int:
    return (
        (number_one ** number_two ** number_three)
        % (number_one * number_three)
    )


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
