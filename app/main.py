from typing import Any, Callable


def cache(func: Callable) -> Any:
    dict_of_results = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        func_arguments = args
        if func_arguments not in dict_of_results:
            print("Calculating new result")
            dict_of_results[func_arguments] = func(*args, **kwargs)
            return dict_of_results[func_arguments]
        else:
            print("Getting from cache")
            return dict_of_results[func_arguments]

    return inner
