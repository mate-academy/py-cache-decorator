from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func.cache_dict: dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in func.cache_dict:
            print("Getting from cache")
            return func.cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func.cache_dict[key] = result
            return result

    return wrapper


@cache
def long_time_function(base_number: int, exponent: int, modulus: int) -> int:
    return (base_number ** exponent ** modulus) % (base_number * modulus)


@cache
def long_time_function_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]


long_time_function(1, 2, 3)
long_time_function(2, 2, 3)
long_time_function_2((5, 6, 7), 5)
long_time_function(1, 2, 3)
long_time_function_2((5, 6, 7), 10)
long_time_function_2((5, 6, 7), 10)
