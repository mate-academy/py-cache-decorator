def cache(func):
    result_cache = {}

    def wrapper(*args):

        if args not in result_cache:
            result_cache[args] = func(*args)
            print("Calculating new result")

        elif args in result_cache:
            print("Getting from cache")

        return result_cache[args]

    return wrapper
