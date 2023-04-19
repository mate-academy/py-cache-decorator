from functools import wraps
from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (func, args, frozenset(kwargs.items()))
        if key in memory:
            print("Getting from cache")
            return memory[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memory[key] = result
            return result

    return wrapper


@cache
def long_time_func(a_value: int, b_value: int, c_value: int) -> int:
    return (a_value ** b_value ** c_value) % (a_value * c_value)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
