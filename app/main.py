def cache(func):
    cache_of_results = {}
    cache_of_funcs = []

    def wrapper(*args, **kwargs):
        if func.__name__ in cache_of_funcs and\
                (str(args) + str(**kwargs)) in cache_of_results:
            print("Getting from cache")
            return cache_of_results[(str(args) + str(**kwargs))]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_of_results.update({(str(args) + str(**kwargs)): result})
            cache_of_funcs.append(str(func.__name__))
            return result
    return wrapper
