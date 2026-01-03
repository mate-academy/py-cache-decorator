from typing import Callable, Any


def cache(func: Callable) -> Callable:
    save_list = []

    def wrapper(*args, **kwargs) -> Any:
        for item in save_list:
            if args in item and kwargs in item:
                print("Getting from cache")
                return item[-1]
        result = func(*args, **kwargs)
        save_list.append([args, kwargs, result])
        print("Calculating new result")
        return result

    return wrapper
