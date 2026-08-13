from typing import Any, Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args: Any) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]

        print("Calculating new result")
        new_result = func(*args)
        result[args] = new_result

        return new_result
    return wrapper
