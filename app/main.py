import copy
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    function_dictionary = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in function_dictionary:
            print("Getting from cache")
            return copy.deepcopy(function_dictionary[key])

        print("Calculating new result")
        result = func(*args, **kwargs)
        function_dictionary[key] = copy.deepcopy(result)
        return result
    return inner


@cache
def long_time_func(alfa: int, betta: int, cell: int) -> int:
    return (alfa ** betta ** cell) % (alfa * cell)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
