from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
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
def long_time_func(aa: int, bb: int, cc: int) -> int:
    return (aa ** bb ** cc) % (aa * cc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
