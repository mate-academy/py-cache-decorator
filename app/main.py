from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            result = func(*args)
            print("Calculating new result")
            func_cache[args] = result
            return result

    return wrapper
