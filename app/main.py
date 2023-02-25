from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_of_results = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in dict_of_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_of_results.update({args: func(*args)})
        return dict_of_results.get(args)

    return wrapper
