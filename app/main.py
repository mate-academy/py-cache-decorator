from typing import Callable, Hashable, ParamSpec, TypeVar

Param = ParamSpec("Param")
RetType = TypeVar("RetType")


def cache(func: Callable[Param, RetType]) -> Callable[Param, RetType]:
    cache_dict: dict = {}

    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> RetType:
        all_arguments = args + tuple(kwargs.values())
        for arg in all_arguments:
            if not isinstance(arg, Hashable):
                return func(*args, **kwargs)
        signature: tuple = (args, tuple(kwargs.items()))
        if signature in cache_dict:
            print("Getting from cache")
            return cache_dict[signature]
        print("Calculating new result")
        cache_dict[signature] = func(*args, **kwargs)
        return cache_dict[signature]

    return wrapper
