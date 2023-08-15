from functools import wraps


def cache(func: callable) -> callable:
    result_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in result_cache:
            print("Getting from cache")
            return result_cache[key]
        else:
            result = func(*args, **kwargs)
            result_cache[key] = result
            print("Calculating new result")
            return result
    return wrapper
