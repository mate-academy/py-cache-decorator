import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cashh = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in cashh:
            print("Getting from cache")
            return cashh[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cashh[args] = result
        return result

    return wrapper


@cache
def add(first_number: int, second_number: int) -> int:
    return first_number + second_number