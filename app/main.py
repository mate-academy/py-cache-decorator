from typing import Callable, Any


def cache(func: Callable) -> Callable:
    function_dictionary = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in function_dictionary:
            print("Getting from cache")
            return function_dictionary[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        function_dictionary[key] = result
        return result
    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]