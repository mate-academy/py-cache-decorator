from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    Decorator for caching results of functions with immutable arguments.

    The `cache` function is designed to automatically cache results of
    functions with immutable (unchangeable) arguments. Each function
    decorated with this decorator gets its own cache to store results.
    In this decorator, the cache is reset with each new test suite.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The modified function that caches results based on
        arguments.

    Examples:
        @cache
        def long_time_func(a: int, b: int, c: int) -> int:
            return (a ** b ** c) % (a * c)
        result = long_time_func(2, 3, 4)  # Computation is performed
                                          # and result is cached
        result = long_time_func(2, 3, 4)  # Result is retrieved from
                                          # cache, computation is not
                                          # repeated

    Note:
        This decorator supports caching results for functions with
        arguments that are immutable types, such as int, float, str,
        tuple, bool, and NoneType. The results are stored in memory
        and used for subsequent calls to the function with the same
        arguments.
    """
    cached_data = {}
    immutable_type = (int, float, str, tuple, bool, type(None))

    def argument_based_cacher(*args) -> Any:
        nonlocal cached_data
        if all([isinstance(variable, immutable_type) for variable in args]):
            func_key = tuple(args)
            if func.__name__ not in cached_data.keys():
                cached_data[func.__name__] = {}
            if func_key in cached_data[func.__name__]:
                print("Getting from cache")
                return cached_data[func.__name__][func_key]
            else:
                print("Calculating new result")
                func_result = func(*args)
                cached_data[func.__name__][func_key] = func_result
                return func_result
        else:
            print("Calculating new result")
            return func(*args)
    return argument_based_cacher
