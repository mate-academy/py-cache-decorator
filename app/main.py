from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:

        func_arguments_and_results = storage.get(func)
        if func in storage and args in func_arguments_and_results:
            print("Getting from cache")
            res = func_arguments_and_results.get(args)
        else:
            res = func(*args)
            print("Calculating new result")
            func_arguments_and_results.update({args: res}) if func in storage \
                else storage.update({func: {args: res}})
        return res

    return inner
