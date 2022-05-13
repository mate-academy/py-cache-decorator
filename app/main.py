def cache(func):
    dict_results = {}

    def wrapper(*args, **kwargs):
        if args in dict_results:
            print("Getting from cache")
            return dict_results[args]

        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_results[args] = result
            return result

    return wrapper
