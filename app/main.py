def cache(func):
    stored_results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_results[key] = result
            return result

    return wrapper
