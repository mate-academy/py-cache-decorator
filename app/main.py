from typing import Callable, Any


def cache(func: Callable) -> Callable:
    args_and_results_dict = {}

    def wrapper(*args) -> Any:
        for args_ in args_and_results_dict.keys():
            if args_ == args:
                print("Getting from cache")
                return args_and_results_dict[args]

        print("Calculating new result")
        result = func(*args)
        args_and_results_dict[args] = result
        return result

    return wrapper
