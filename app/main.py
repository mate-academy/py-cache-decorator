from typing import Callable, Any


def cache(func: Callable) -> Callable:
    operations = {}

    def wrapper(*args: Any) -> Any:
        if args in operations:
            print("Getting from cache")
            return operations[args]
        else:
            print("Calculating new result")
            result = func(*args)
            operations[args] = result
            return result

    return wrapper
