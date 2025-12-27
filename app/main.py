from typing import Callable, Any


def cache(func: Callable) -> Callable:
    fun_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in fun_cache:
            print("Getting from cache")
            return fun_cache[args]
        print("Calculating new result")
        result = func(*args)
        fun_cache[args] = result
        return result

    return wrapper
