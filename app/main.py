from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args

        if key in storage:
            print("getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result
    return wrapper


@cache
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:
    return (first_num ** second_num ** third_num) % (first_num * third_num)
