from functools import wraps

def cache(func: callable) -> callable:
    history = {}
    @wraps(func)
    def wrapper(*args, **kwargs) -> tuple:
        kw_parameters = tuple(kwargs.items())
        func_id = (func.__name__, args, kw_parameters)
        if func_id in history:
            print("Getting from cache")
            return history[func_id]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            history[func_id] = result
            return result
    return wrapper
