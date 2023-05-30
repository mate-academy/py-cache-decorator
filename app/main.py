 def cache(func: callable) -> callable:
    results = {}

    def inner(*args, **kwargs) -> callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            results[key] = res
        return results[key]
    return inner
