from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        args_tuple = tuple(args)
        if args_tuple in cached_results:
            print("Getting from cache")
            return cached_results[args_tuple]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[args_tuple] = result
            return result

    return wrapper


@cache
def long_time_func(a_one: int, b_one: int, c_one: int) -> int:
    return (a_one ** b_one ** c_one) % (a_one * c_one)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
