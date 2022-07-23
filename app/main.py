def cache(func):
    calls_cache = {}

    def wrapper(*args):
        nonlocal calls_cache
        call_key = func.__name__ + "_".join([str(item) for item in args])

        if call_key in calls_cache:
            res = calls_cache[call_key]
            print("Getting from cache")
        else:
            res = func(*args)
            calls_cache[call_key] = res
            print("Calculating new result")

        return res

    return wrapper
