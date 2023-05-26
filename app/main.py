def cache(func):
    results = {}

    def inner(*args, **kwargs) -> callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result

    return inner
