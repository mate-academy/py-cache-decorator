def cache(func: any) -> any:
    cache_dict = {}

    def wrapper(*args: int) -> any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        cache_dict[args] = func(*args)
        print("Calculating new result")
        return cache_dict[args]
    return wrapper
