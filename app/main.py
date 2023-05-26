def cache(func):
    results = {}

    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            results[key] = res
            return result

    return inner
