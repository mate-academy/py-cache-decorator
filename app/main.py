def cache(func):
    cache_result = {}

    def wripper(*args):
        if args not in cache_result:
            result_func_args = func(*args)
            cache_result[args] = result_func_args
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_result[args]
    return wripper
