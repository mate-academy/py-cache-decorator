from typing import Callable, Any


def cache(func: Callable) -> None:
    result_dict = {}

    def cache_wrapper(*args, **kwargs) -> Any:
        if args not in result_dict:
            result_dict.update({args: func(*args)})
            print("Calculating new result")
            return result_dict[args]

        print("Getting from cache")
        return result_dict[args]

    return cache_wrapper
