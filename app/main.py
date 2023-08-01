from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper


@cache
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:
    return (first_num ** second_num ** third_num) % (first_num * third_num)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
