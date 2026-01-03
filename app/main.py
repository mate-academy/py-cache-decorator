from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:
        information = data.get((args, tuple(sorted(kwargs.items()))))

        if information is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data[(args, tuple(kwargs.items()))] = result

            return result
        else:
            print("Getting from cache")

        return information
    return wrapper
