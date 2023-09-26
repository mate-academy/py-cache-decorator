def cache(func: int) -> int:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> int:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

    return wrapper
