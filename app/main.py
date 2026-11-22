from functools import wraps
from inspect import Parameter, signature
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}
    func_signature = signature(func)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        bound_arguments = func_signature.bind(*args, **kwargs)
        key = tuple(
            (name, value) if func_signature.parameters[name].kind
            != Parameter.VAR_KEYWORD
            else (name, tuple(sorted(value.items())))
            for name, value in sorted(bound_arguments.arguments.items())
        )

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper
