from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args_1: tuple) -> Any:
        def save_result_in_cache(*args_2: tuple) -> bool:
            if args_2 not in cache_dict.keys():
                cache_dict[args_2] = func(*args_2)
                return True
            return False
        was_calculating = save_result_in_cache(*args_1)
        print(
            "Calculating new result" if
            was_calculating else "Getting from cache"
        )
        return cache_dict[*args_1]
    return wrapper
