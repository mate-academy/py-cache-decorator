from typing import Callable


def cache(func: Callable) -> Callable:
    dictionary_result = {}

    def wrapper(*args) -> dict:
        if args in dictionary_result:
            print("Getting from cache")
            return dictionary_result[args]

        print("Calculating new result")

        result = func(*args)
        dictionary_result[args] = result

        return result

    return wrapper
