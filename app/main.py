from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    dic = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in dic:
            print("Getting from cache")
            return dic[args]
        result = func(*args)
        dic[args] = result
        print("Calculating new result")
        return result
    return wrapper
