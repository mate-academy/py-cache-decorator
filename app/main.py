from typing import Callable, Any

cache_archive = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        save_func_done = f"{func} {args} {kwargs}"
        if save_func_done in cache_archive.keys():
            print("Getting from cache")
            res = cache_archive[save_func_done]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache_archive[save_func_done] = res

        return res

    return wrapper
