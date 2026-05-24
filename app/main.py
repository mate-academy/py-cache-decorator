from typing import Callable, Any


def check_in_cache(run_results: dict, func: Callable, *args: Any,
                   **kwargs: Any, ) -> dict:
    if args in run_results:
        print("Getting from cache")
    else:
        print("Calculating new result")
        run_results[args] = func(*args, **kwargs)
    return run_results[args]


def cache(func: Callable) -> Callable:
    run_results = {}

    def wrapper(*args: Any, **kwargs: Any) -> dict:
        cache_answer = check_in_cache(run_results, func, *args, **kwargs)
        return cache_answer

    return wrapper
