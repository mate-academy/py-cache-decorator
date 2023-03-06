from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = dict()

    def inner(*args) -> Any:
        for _ in args:
            if not type(_) in {int, float, tuple, str}:
                return inner
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        results.update({args: func(*args)})
        return results[args]
    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
