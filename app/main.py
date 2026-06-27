from typing import Any, Callable


def cache(func: Callable) -> Callable:
    saved = {}

    def wrapper(*args: Any) -> Any:
        if args in saved:
            print("Getting from cache")
            return saved[args]

        print("Calculating new result")
        result = func(*args)
        saved[args] = result
        return result

    return wrapper
