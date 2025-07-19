from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wraper(*args: Any, **kwargs: Any) -> str:
        if (args, frozenset(kwargs.items())) in cache_dict:
            print("Getting from cache")
            return cache_dict.get((args, frozenset(kwargs)))
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[(args, frozenset(kwargs))] = result
            return result

    return wraper
