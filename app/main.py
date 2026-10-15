from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        tuple_kwargs = tuple(sorted(kwargs.items()))
        tuple_a_and_k = (args, tuple_kwargs)
        if tuple_a_and_k in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[tuple_a_and_k] = func(*args, **kwargs)
        return cache_dict[tuple_a_and_k]
    return wrapper
