from typing import Callable


def cache(func: Callable) -> Callable:
    function_result = {}

    def inner(*args, **kwargs) -> Callable:

        str_arg = str(args)
        str_kward = "".join(str(v) for v in kwargs.values())

        function_call_name = f"{func.__name__}({str_arg}, {str_kward})"
        cached_result = function_result.get(function_call_name)

        if cached_result is not None:
            print("Getting from cache")
            return cached_result
        else:
            print("Calculating new result")
            computated_result = func(*args, **kwargs)
            function_result[function_call_name] = computated_result
            return computated_result

    return inner
