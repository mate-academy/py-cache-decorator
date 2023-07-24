from typing import Callable, Any


def cache(func: Callable) -> Any:
    result = {}

    def check_data(*args: int) -> Callable:
        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args)
            print("Calculating new result")
        return result[args]
    return check_data
