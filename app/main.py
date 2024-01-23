from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> int:
        piece_of_data = (args, frozenset(kwargs.items()))
        if piece_of_data in cache_dict:
            print("Getting from cache")
            return cache_dict[piece_of_data]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[piece_of_data] = result
            return result

    return wrapper
