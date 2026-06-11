from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results_cache = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(kwargs.items()))

        if cache_key not in results_cache:
            print("Calculating new result")
            results_cache[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return results_cache[cache_key]

    return inner
