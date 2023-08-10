from typing import Callable, Hashable, ParamSpec, TypeVar

Param = ParamSpec("Param")
RetType = TypeVar("RetType")


def cache(func: Callable[Param, RetType]) -> Callable[Param, RetType]:
    cache_dict: dict = {}

    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> RetType:
        for arg in args:
            if not isinstance(arg, Hashable):
                return func(*args, **kwargs)
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        cache_dict[args] = func(*args, **kwargs)
        return cache_dict[args]

    return wrapper
