from functools import wraps
from typing import Any, Callable, Dict, Tuple, Hashable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Hashable) -> Any:
        if args in cache:
            print("Getting from cache")
            return cache[args]

        print("Calculating new result")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper
