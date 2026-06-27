from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = dict()
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in result.keys():
            print("Getting from cache")
            return result[args]
        else:
            result[args] = func(*args, **kwargs)
            print("Calculating new result")
            return result[args]
    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
