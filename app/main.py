def cache(func):
    stored_results = {}

    def wrapper(*args):
        if func.__name__ not in stored_results:
            stored_results[func.__name__] = {}

        arg_tuple = args

        if args in stored_results[func.__name__]:
            print("Getting from cache")
            return stored_results[func.__name__][arg_tuple]
        else:
            print("Calculating new result")
            result = func(*args)
            stored_results[func.__name__][arg_tuple] = result
            return result

    return wrapper
