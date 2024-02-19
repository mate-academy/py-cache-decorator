from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:  # any because unknown return type
        cache_key = f"args={args} kwargs={kwargs}"
        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        cached_results[cache_key] = func(*args, **kwargs)
        print("Calculating new result")

        return cached_results[cache_key]

    return wrapper
