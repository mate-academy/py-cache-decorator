def cache(func):
    calls_cache = {}

    def wrapper(*args):
        if args in calls_cache:
            res = calls_cache[args]
            print("Getting from cache")
        else:
            res = func(*args)
            calls_cache[args] = res
            print("Calculating new result")

        return res

    return wrapper
