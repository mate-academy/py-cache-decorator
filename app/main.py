from typing import Any


def cache(func: callable) -> callable:
    cached_results = {}

    def inner(*args: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results.update({args: func(*args)})
        return cached_results[args]

    return inner
