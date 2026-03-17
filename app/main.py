from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args) -> any:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
