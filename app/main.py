from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        if args in result_dict:
            print("Getting from cache")
            result = result_dict[args]
            return result

        print("Calculating new result")
        result = func(*args, **kwargs)
        result_dict[args] = result
        return result

    return inner
