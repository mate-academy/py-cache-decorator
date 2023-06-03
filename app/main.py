from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    memo = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs))
        if key in memo:
            print("Getting from cache")
            return memo[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            memo[key] = res
            return res

    return wrapper
