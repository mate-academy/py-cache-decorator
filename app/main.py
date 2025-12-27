# from typing import Callable
#
#
# def cache(func: Callable[[], int]) -> Callable[[], int]:
def cache(func: callable) -> callable:
    data = {}

    def action(*args, **kwargs) -> int:
        if (f"{func}{args}{kwargs}") in data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data[f"{func}{args}{kwargs}"] = func(*args, **kwargs)
        return data[f"{func}{args}{kwargs}"]

    return action
