def cache(func):
    dict_results = {}

    def wrapper(*args):
        if args in dict_results:
            print("Getting from cache")
            return dict_results[args]
        print("Calculating new result")
        result = func(*args)
        dict_results.update({args: result})
        return result
    return wrapper
