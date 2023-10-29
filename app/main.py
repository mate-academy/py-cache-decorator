from typing import Any, Callable


def cache(func: Callable) -> Callable:
    funct_results_cache = {}

    def wpapper_func(*args) -> Any:
        if args in funct_results_cache.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            funct_results_cache[args] = func(*args)
        return funct_results_cache[args]
    return wpapper_func
