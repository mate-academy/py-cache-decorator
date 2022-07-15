from functools import wraps


def cache(func):
    function_results = {}

    @wraps(func)
    def func_wrapper(*args):
        if args in function_results:
            print("Getting from cache")
        else:
            result = func(*args)
            function_results[args] = result
            print("Calculating new result")
        return function_results[args]

    return func_wrapper
