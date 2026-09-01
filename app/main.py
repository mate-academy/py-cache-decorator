from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Callable:
        key = (func, *args)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args)
        cache_dict[key] = result
        return result
    return wrapper


@cache
def pafon_test(number1: int, number2: int) -> float:
    return number1 / number2


@cache
def pafon_test2(number1: int, number2: int) -> float:
    return number1 * number2


pafon_test(1, 1)
pafon_test(1, 1)
pafon_test2(1, 1)
pafon_test2(1, 1)
