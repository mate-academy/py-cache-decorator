from typing import Callable, Any


def cache(func: Callable) -> Callable:
    all_cash = {}

    def inner_func(*args) -> Any:
        if args in all_cash:
            print("Getting from cache")
            return all_cash[args]
        # not in cash
        print("Calculating new result")
        res_of_func = func(*args)
        all_cash[args] = res_of_func
        return res_of_func
    return inner_func
