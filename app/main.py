from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> int:
        if func in results and args in results[func]:
            print("Getting from cache")
            return results[func][args]
        print("Calculating new result")
        result = func(*args)
        if func not in results:
            results[func] = {}
        results[func][args] = result
        return result

    return wrapper
