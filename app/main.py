def cache(func):
    cache_dict = {}

    def wrap_cache(*args):
        stored_result = cache_dict.get(args, False)
        if args in cache_dict:
            print("Getting from cache")
            return stored_result
        else:
            print("Calculating new result")
            func_result = func(*args)
            cache_dict[args] = func_result
            return func_result

    return wrap_cache
