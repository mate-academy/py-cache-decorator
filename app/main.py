def cache(func):
    cache_results = {}

    def wrapped(*args, **kwargs):
        function_args = tuple([*args])
        if function_args not in cache_results:
            res = func(*args)
            cache_results[function_args] = res
            print("Calculating new result")
            return res
        print("Getting from cache")
        return cache_results[function_args]

    return wrapped
