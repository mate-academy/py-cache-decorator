from typing import Callable


def cache(func: Callable) -> Callable:
    caching_result = {}

    def wrapper(*args) -> Callable:
        if args in caching_result:
            print("Getting from cache")
            return caching_result[args][0]
        print("Calculating new result")
        result_func = func(*args)
        caching_result[args] = (caching_result.get(args, []) + [result_func])
        return result_func
    return wrapper
