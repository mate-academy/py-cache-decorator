def cache(func):
    results = {}

    def inner(*args, **kwargs):
        key = str(args)
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            res[key] = res
            return res

    return inner
