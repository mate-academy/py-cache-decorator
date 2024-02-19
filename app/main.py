from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:  # any because unknown return type
        cache_key = f"args={args} kwargs={kwargs}"
        nonlocal cached_results
        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        print("Calculating new result")

        return result

    return wrapper
