def cache(func: callable) -> callable:
    cache_dict = {}

    def inner(*args: any) -> callable:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(args)
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args)
            return cache_dict.get(args)
    return inner
