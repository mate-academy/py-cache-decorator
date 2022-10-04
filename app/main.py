def cache(func):
    result_cache = {}

    def wrapper(*args):
        if args not in result_cache:
            result_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return result_cache[args]
    return wrapper
