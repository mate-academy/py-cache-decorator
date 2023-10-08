from typing import Callable, Any, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results_cache = {}

    def wrapper(*args: Tuple, **kwargs: Any) -> Any:

        key = (args, frozenset(kwargs.items()))

        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result
            return result

    return wrapper
