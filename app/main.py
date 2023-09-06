from functools import wraps


def cache(func: callable) -> callable:
    dictionary = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any :
        if args in dictionary:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dictionary[*args] = func(*args)
        return dictionary[*args]
    return wrapper
