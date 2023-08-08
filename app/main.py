def cache(func: callable) -> callable:
    dict_cache = {}

    def inner(*args, **kwargs) -> str:
        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        else:
            result = func(*args, **kwargs)
            dict_cache[args] = result
            print("Calculating new result")
            return result

    return inner
