def cache(func):
    stored_results = {}

    def wrapper(*args):
        if args in stored_results:
            print("Getting from cache")
        else:
            stored_results.update({args: func(*args)})
            print("Calculating new result")
        return stored_results[args]
    return wrapper
