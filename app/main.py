from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_runs = {}

    def wrapper(*args, **kwargs) -> Any:
        run_key = f"{args} {kwargs}"
        if run_key not in stored_runs:
            stored_runs[run_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stored_runs[run_key]
    return wrapper
