from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def make_key(args: Any, kwargs: Any) -> Any:
        return (args, tuple(kwargs.items()))

    def wrapper(*args: Any, **kwargs: Any):
        key = make_key(args, kwargs)

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * second)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
