from typing import Any, Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args: Any) -> Any:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        print("Calculating new result")
        stored_results[args] = func(*args)
        return stored_results[args]

    return wrapper


@cache
def long_time_func(base: int, power: int, mod: int) -> int:
    return (base ** power ** mod) % (base * mod)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
