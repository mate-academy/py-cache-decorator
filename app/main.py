from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = dict()

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
            return result[key]
    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
