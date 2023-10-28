from typing import Callable, Any


cached_func = {}


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        key = (func, args, frozenset(kwargs.items()))
        if key in cached_func:
            print("Getting from cache")
            return cached_func[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cached_func[key] = res
        return res
    return inner
