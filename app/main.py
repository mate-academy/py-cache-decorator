from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args) -> Any:
        for key, value in result_dict.items():
            if key == args:
                print("Getting from cache")
                return value

        res_fun = func(*args)
        result_dict[args] = res_fun
        print("Calculating new result")
        return res_fun

    return inner
