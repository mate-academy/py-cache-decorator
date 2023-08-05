from typing import Any, Tuple, Dict


def cache(func: callable) -> callable:
    cached_results: Dict[Tuple, Any] = {}

    def wrapper(*args: Tuple, **kwargs: Dict) -> Any:
        key: Tuple = args + tuple(kwargs.items())
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result: Any = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper
