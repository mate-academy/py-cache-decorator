from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result
            print("Calculating new result")
            return result

    return wrapper


@cache
def long_time_func(time_a: int, time_b: int, time_c: int) -> int:
    return (time_a ** time_b ** time_c) % (time_a * time_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
