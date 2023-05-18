from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    run_log = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if func.__name__ not in run_log:
            print("Calculating new result")
            func_result = func(*args)
            run_log.update(
                {
                    func.__name__: [
                        {
                            args: func_result
                        }
                    ]
                }
            )
            return func_result
        for data in run_log[func.__name__]:
            if args in data:
                print("Getting from cache")
                return data[args]
        print("Calculating new result")
        func_result = func(*args)
        run_log[func.__name__].append(
            {
                args: func_result
            }
        )
        return func_result

    return wrapper
