from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        key_args = args

        if func_name not in wrapper.results:
            wrapper.results[func_name] = {}

        if key_args not in wrapper.results[func_name]:
            value_result = func(*args, **kwargs)
            new_dict = {key_args: value_result}
            wrapper.results[func_name].update(new_dict)
            print("Calculating new result")

        else:
            print("Getting from cache")

        return wrapper.results[func_name][key_args]

    wrapper.results = {}
    return wrapper
