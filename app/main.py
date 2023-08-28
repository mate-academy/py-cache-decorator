from functools import wraps
from typing import Any, Tuple, Dict, Callable


def cache(func: Callable) -> Callable:
    results: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        arguments = args + tuple(kwargs.items())
        if arguments in results:
            print("Getting from cache")
            return results[arguments]
        else:
            result = func(*args, **kwargs)
            results[arguments] = result
            print("Calculating new result")
            return result
    return wrapper
