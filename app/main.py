from typing import Callable


def cache(func: Callable) -> Callable:
    previous_runs = {}

    def inner(*args) -> object:
        hash_key = args
        if hash_key in previous_runs.keys():
            print("Getting from cache")
            return previous_runs[hash_key]
        print("Calculating new result")
        result = func(*args)
        previous_runs[hash_key] = result
        return result

    return inner
