from typing import Callable


def cache(func: Callable) -> Callable:
    previous_runs = {}

    def inner(*args) -> object:
        nonlocal previous_runs
        hash_key = hash_function(func, args)
        if hash_key in previous_runs.keys():
            print("Getting from cache")
            return previous_runs[hash_key]
        else:
            print("Calculating new result")
            result = func(*args)
            previous_runs[hash_key] = result
        return result

    return inner


def hash_function(function_to_hash: Callable, args: tuple):
    """
    Hashing incoming function, using it's name
    and arguments with a string result.
    No encryption.
    """
    name_of_hashed = str(function_to_hash.__name__)
    hashed_args = str(args)
    result_hash = name_of_hashed + hashed_args
    return result_hash
