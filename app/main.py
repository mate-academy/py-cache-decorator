from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:

    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sorted_kwargs = tuple(sorted(kwargs.items()))
        ceche_key = (args, sorted_kwargs)
        if ceche_key in storage:
            print("Getting from cache")
            return storage[ceche_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[ceche_key] = result
            return result
    return wrapper


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
