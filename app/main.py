from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cashed_result = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args not in cashed_result:
            print("Calculating new result")
            cashed_result[args] = func(*args, **kwargs)
            return cashed_result[args]
        else:
            print("Getting from cache")
            return cashed_result[args]
    return wrapper
