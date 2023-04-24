from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # data_cache == {args: [func_name, result]}
    data_cache = dict()

    def init(*args) -> Any:
        for key, value in data_cache.items():
            if key == args and value[0] == func.__name__:
                print("Getting from cache")
                return value[1]
        print("Calculating new result")
        data_cache[args] = [func.__name__, func(*args)]
        return data_cache[args][1]  # The result was calculated above
    return init
