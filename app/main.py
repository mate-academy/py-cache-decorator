from typing import Any, Dict, Tuple


def cache(func: callable) -> callable:
    cached_results: Dict[Tuple[str, Tuple, frozenset], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key: Tuple[str, Tuple, frozenset] = (func.__name__, args,
                                             frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            result: Any = func(*args, **kwargs)
            cached_results[key] = result
            print("Calculating new result")
            return result

    return wrapper
