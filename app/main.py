def cache(func: list) -> str:
    cache_dict = {}

    def wrapps(*args, **kwargs) -> str:
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[args]
    return wrapps
