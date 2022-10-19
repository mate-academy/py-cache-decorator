from typing import Union


def cache(func: callable) -> callable:
    saved_results = {}

    def wrapper(*args: Union[int, float, str, tuple, frozenset],
                **kwargs: Union[int, float, str, tuple, frozenset]) -> dict:
        if args in saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_results[args] = func(*args, **kwargs)

        return saved_results[args]
    return wrapper
