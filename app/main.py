from typing import Callable, Any


def cache(func: Callable) -> Any:
    sum_func = {}

    def wrapped(*arg) -> dict:
        if arg not in sum_func:
            some_work_func = func(*arg)
            sum_func[arg] = some_work_func
            print("Calculating new result")
            return some_work_func
        else:
            print("Getting from cache")
            return sum_func[arg]
    return wrapped
