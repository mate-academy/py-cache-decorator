from typing import Callable, Any


def cache(func: Callable) -> Any:
    all_number = []
    result = {}

    def check_data(*args: int) -> Callable:
        if args in all_number:
            print("Getting from cache")
        else:
            result[f"{func.__name__}{args}"] = func(*args)
            all_number.append(args)
            print("Calculating new result")
        return result[f"{func.__name__}{args}"]
    return check_data

