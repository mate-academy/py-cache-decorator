from typing import Callable


def cache(func: Callable) -> Callable:

    results = {}

    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (
            args,
            tuple((key, value) for key, value in sorted(kwargs.items()))
        )

        if cache_key in results:
            print("Getting from cache")

            return results[cache_key]

        result = func(*args, **kwargs)
        results.update({cache_key: result})
        print("Calculating new result")
        return result
    return wrapper
