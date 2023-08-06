def cache(func: callable) -> callable:
    dict_cache = {}

    def inner(*args, **kwargs) -> int:
        key = (args, tuple(kwargs.items()))
        if key in dict_cache:
            print("Getting from cache")
            return dict_cache[key]
        else:
            result = func(*args, **kwargs)
            dict_cache[key] = result
            print("Calculating new result")
            return result

    return inner
