def cache(func):
    stored_results = {}

    def wrapper(*args):

        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]

        result = func(*args)
        stored_results.update({args: result})
        print("Calculating new result")
        return result

    return wrapper
