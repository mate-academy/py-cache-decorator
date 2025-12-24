from typing import Callable, Any


def cache(func: Callable) -> Callable:
    _cache: dict[tuple[Any, ...], Any] = {}

    def wrapper(*args: Any) -> Any:
        if args in _cache:
            print("Getting from cache")
            return _cache[args]
        print("Calculating new result")
        result = func(*args)
        _cache[args] = result
        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple[int, ...], power: int) -> list[int]:
    return [number ** power for number in n_tuple]
