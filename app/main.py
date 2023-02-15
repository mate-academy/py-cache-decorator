import functools


def cache(func: callable) -> any:
    stored_param_and_result = {}

    @functools.wraps(func)
    def inner(*args) -> any:
        nonlocal stored_param_and_result
        if args in stored_param_and_result.keys():
            print("Getting from cache")
            return stored_param_and_result[args]
        else:
            stored_param_and_result[args] = func(*args)
            print("Calculating new result")
            return stored_param_and_result[args]

    return inner
