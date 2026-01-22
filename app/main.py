from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def longtime_function(*args: Any, **kwargs: Any) -> Any:

        for arg in args:
            if isinstance(arg, (int, float, str, bool, tuple)):
                if args not in cache_dict:
                    print("Calculating new result")
                    result_function = func(*args)
                    cache_dict[args] = result_function
                    return result_function
                else:
                    print("Getting from cache")
                    return cache_dict[args]
            else:
                print("This is mutable!")
                break

        for kwarg in kwargs:
            if isinstance(kwarg, (int, float, str, bool, tuple)):
                if kwargs not in cache_dict:
                    print("Calculating new result")
                    result_function = func(**kwargs)
                    cache_dict[kwargs] = result_function
                    return result_function
                else:
                    print("Getting from cache")
                    return cache_dict[kwargs]
            else:
                print("This is mutable!")
                break

    return longtime_function
