from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in results_dict:
            print("Getting from cache")
            return results_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_dict[args] = result
            return result

    return wrapper
