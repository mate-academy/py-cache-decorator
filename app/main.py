from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Any:

        key = (args, frozenset(kwargs.items()))

        if key in results_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result

        return results_cache[key]

    return wrapper
