def cache(func: str) -> any:
    cache_decorator = {}

    def wrapper(*args, **kwargs) -> any:
        args_key = tuple(args)
        kwargs_key = tuple(kwargs.items())
        key = (args_key, kwargs_key)

        if key in cache_decorator:
            print("Getting from cache")
            return cache_decorator[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_decorator[key] = result
            return result
    return wrapper
