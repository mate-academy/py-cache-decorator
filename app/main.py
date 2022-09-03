def cache(func):
    results = {}

    def wrapper(*args, **kwargs):
        if isinstance(args, list) or isinstance(args, dict)\
                or isinstance(args, set):
            return "This function isn't working with mutable arguments"
        else:
            if args in results:
                print("Getting from cache")
            else:
                print("Calculating new result")
                results[args] = func(*args)

            return results[args]

    return wrapper
