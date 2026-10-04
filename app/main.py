from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs: Any) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        elif args not in cache_data:
            print("Calculating new result")
            cache_data[args] = func(*args, **kwargs)
            return cache_data[args]
    return wrapper


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


print(long_time_func_2((5, 6, 7), 10))
print(long_time_func_2((5, 6, 7), 10))
