from typing import Callable


def cache(func: Callable) -> Callable:
   from functools import wraps
from typing import Callable, Any

def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Convertimos kwargs a una tupla ordenada para que sea hashable y sirva como clave
        key = (args, tuple(sorted(kwargs.items())))

        if key in memo:
            print("Getting from cache")
            return memo[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[key] = result
        return result

    return wrapper
   
