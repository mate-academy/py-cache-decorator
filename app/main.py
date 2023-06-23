from functools import wraps
from typing import Any, Tuple, Dict


def cache(func: callable) -> callable:
    results: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key: Tuple[Any, ...] = args + tuple(sorted(kwargs.items()))

        if key in results:
            print("Getting from cache")
            return results[key]

        print("Calculating new result")
        result: Any = func(*args, **kwargs)
        results[key] = result
        return result

    return wrapper
