from typing import Any


def cache(func: Any) -> Any:
    dt = {}

    def wrapper(*args) -> Any:
        if args in dt:
            print("Getting from cache")
            return dt[args]
        else:
            result = func(*args)
            dt[args] = result
            print("Calculating new result")
            return result

    return wrapper
