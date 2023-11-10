from typing import Callable, Union, List, Tuple


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Union[int, List[int]]:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")
            return result

    return wrapper


@cache
def long_time_func(par_a: int, par_b: int, par_c: int) -> int:
    return (par_a ** par_b ** par_c) % (par_a * par_c)


@cache
def long_time_func_2(n_tuple: Tuple[int, int, int], power: int) -> List[int]:
    return [number ** power for number in n_tuple]
