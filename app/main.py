def cache(func):
    cache_of_results = {}
    cache_of_funcs = []

    def wrapper(*args, **kwargs):
        all_args = str(args) + str(**kwargs)
        if func.__name__ in cache_of_funcs and all_args in cache_of_results:
            print("Getting from cache")
            return cache_of_results[all_args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_of_results.update({all_args: result})
            cache_of_funcs.append(str(func.__name__))
            return result
    return wrapper
