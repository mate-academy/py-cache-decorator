from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args) -> Any:
        for key in result_dict:
            if args in result_dict:
                print("Getting from cache")
                return result_dict[args]

        res_fun = func(*args)
        result_dict[args] = res_fun
        print("Calculating new result")
        return res_fun

    return inner
