from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # Use private dictionary unique to each function decorated
    # It lives across executions because of closure scope memory
    storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Create a unique, hashable key the storage dict by combining
        # positional and keyword arguments
        cache_key = (args, tuple(sorted(kwargs.items())))

        # Check if this exact call signature already exists in storage
        if cache_key in storage:
            print("Getting from cache")
            return storage[cache_key]

        # If it's a completely original call, compute the new result
        print("Calculating new result")
        result = func(*args, **kwargs)

        # Store the fresh result in the dictionary before returning it
        storage[cache_key] = result
        return result

    return wrapper


@cache
def long_time_func(int_one: int, int_two: int, int_three: int) -> int:
    return (int_one ** int_two ** int_three) % (int_one * int_three)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
