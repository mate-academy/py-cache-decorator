from functools import wraps


def cache(func):
    function_results = {}

    @wraps(func)
    def func_wrapper(*args):
        if func.__name__ in function_results and \
                args in function_results[func.__name__]:
            print("Getting from cache")
        else:
            result = func(*args)
            function_results.setdefault(func.__name__, {args: result})
            function_results[func.__name__][args] = result
            print("Calculating new result")
        return function_results[func.__name__][args]

    return func_wrapper
