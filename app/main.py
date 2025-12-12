from functools import wraps
from typing import Callable


cache_dict = dict()


def read_cache_dict() -> dict:
    result = cache_dict
    return result


def cache(func: Callable) -> Callable:
    func_name = func.__name__

    @wraps(func)
    def wrapper(*args) -> list:
        one_key_list = [func_name, args]
        one_key = tuple(one_key_list)
        result_inner = cache_dict.get(one_key)
        if result_inner is None:
            print("Calculating new result")
            result_inner = func(*args)
            cache_dict[one_key] = result_inner
        else:
            print("Getting from cache")
        # save_cache_dict(cache_dict)
        return result_inner

    clean_cache_dict()
    return wrapper


def clean_cache_dict() -> None:
    global cache_dict
    cache_dict = dict()
