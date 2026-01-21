from typing import Callable
import pickle


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def wrapper(*args) -> Callable:
        key = pickle.dumps(args)
        if key in cache_dictionary:
            print("Getting from cache")
            return cache_dictionary[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_dictionary[key] = result
            return result
    return wrapper
