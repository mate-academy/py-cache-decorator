from typing import Callable, Any
from functools import wraps
import threading
import pickle


def cache(func: Callable) -> Callable:
    cache_dict = {}
    lock = threading.Lock()

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = pickle.dumps((args, kwargs))
        with lock:
            if key in cache_dict:
                print("Getting from cache")
                return cache_dict[key]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                cache_dict[key] = result
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
