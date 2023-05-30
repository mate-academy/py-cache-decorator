from typing import Callable, Union, Tuple


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args: Union[int, Tuple[int, float]]) -> Union[int, list]:
        if args in results:
            print("Getting from cache")
            return results[args]

        results[args] = func(*args)
        print("Calculating new result")
        return results[args]
    return inner


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[int]:
    return [number ** power for number in n_tuple]
