from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args: Any) -> Any:
        if args not in result:
            print("Calculating new result")
            result[args] = func(*args)
        else:
            print("Getting from cache")

        return result.get(args)

    return wrapper
