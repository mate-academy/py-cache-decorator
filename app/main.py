from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func_list = {}

    def wrapper(*args: Any) -> Any:
        if args not in func_list.keys():
            func_list[args] = func(*args)
            func_result = func_list.get(args)
            print("Calculating new result")

            return func_result
        print("Getting from cache")
        return func_list.get(args)

    return wrapper
