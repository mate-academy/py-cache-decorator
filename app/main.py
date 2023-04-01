import time
from typing import Callable


def cache(func: Callable) -> Callable:

    cache_storage = {}

    def wrapper(*args, **kwargs) -> any:
        key = (func, args, frozenset(kwargs.items()))
        if key not in cache_storage:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
        else:
            print("Getting from cache")

        return cache_storage[key]

    return wrapper


@cache
def long_time_func(aa: int, bb: int, cc: int) -> int:
    return (aa ** bb ** cc) % (aa * cc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":
    start_time = time.time()
    result = cache()
    end_time = time.time()
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
