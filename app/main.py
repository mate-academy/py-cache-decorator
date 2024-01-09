from functools import wraps
from typing import Any, Callable, Tuple, Union


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args: Union[int, float, str, bool, Tuple]) -> Any:
        if args in results:
            print("Getting from cache")

            return results[args]
        else:
            print("Calculating new result")
            results[args] = func(*args)

            return results[args]

    return wrapper
