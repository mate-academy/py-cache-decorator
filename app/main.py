from functools import wraps
from typing import Callable, TypeVar, ParamSpec

ParamSpecArgs = ParamSpec("ParamSpecArgs")
ReturnType = TypeVar("ReturnType")


def cache(
    func: Callable[ParamSpecArgs, ReturnType]
) -> Callable[ParamSpecArgs, ReturnType]:
    _cache = {}

    @wraps(func)
    def wrapper(
        *args: ParamSpecArgs.args, **kwargs: ParamSpecArgs.kwargs
    ) -> ReturnType:
        key = (args, tuple(sorted(kwargs.items())))
        if key in _cache:
            print("Getting from cache")
            return _cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _cache[key] = result
            return result

    return wrapper
