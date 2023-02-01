from typing import Callable, Any


def cache(func: Callable) -> Callable:
    operations = {}

    def wrapper(*args: Any) -> Any:
        if args in operations:
            print("Getting from cache")
        else:
            print("Calculating new result")
            operations[args] = func(*args)

        return operations[args]

    return wrapper
