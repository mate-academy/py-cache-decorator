from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    _cache: Dict[Tuple[Tuple[Any, ...], Tuple[Tuple[str, Any], ...]], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key_args = args
        key_kwargs = tuple(sorted(kwargs.items()))
        cache_key = (key_args, key_kwargs)

        if cache_key in _cache:
            print("Getting from cache")
            return _cache[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        _cache[cache_key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]
