from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key not in result:
            print("Calculating new result")
            result2 = func(*args, **kwargs)
            result[key] = result2
            return result2
        else:
            print("Getting from cache")
            return result[key]
    return wrapper


@cache
def long_time_func(base: int, exponent: int, factor: int) -> int:
    return (base ** exponent ** factor) % (base * factor)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


if __name__ == "__name__":
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)
