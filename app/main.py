def cache(func):
    results = {}

    def inner(*args, **kwargs):
        key = str(args)
        print(key)
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return inner
