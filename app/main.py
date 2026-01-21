from typing import Callable


def cache(func: Callable) -> Callable:

    results = {}

    def inner(*args, **kwargs) -> None:

        key = (args, frozenset(kwargs.items()))

        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result
        return result

    return inner


@cache
def long_time_func(int1: int, int2: int, int3: int) -> int:
    return (int1 ** int2 ** int3) % (int1 * int3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
