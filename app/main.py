def cache(func: str) -> any:
    cache = {}

    def wrapper(*args, **kwargs) -> any:
        args_key = tuple(args)
        kwargs_key = tuple(kwargs.items())
        key = (args_key, kwargs_key)

        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

