from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dct = {}

    def inner(*args: Any) -> int:
        if args in dct:
            print("Getting from cache")
            return dct[args]

        print("Calculating new result")
        result = func(*args)
        dct[args] = result
        return result

    return inner


@cache
def long_time_func(aa: int, bb: int, cc: int) -> int:
    return (aa ** bb ** cc) % (aa * cc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
