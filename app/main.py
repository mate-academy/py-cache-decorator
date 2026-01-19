def cache(func: callable) -> callable:
    results = {}

    def inner(*args, **kwargs) -> callable:
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            results[key] = func(*args, **kwargs)
            print("Calculating new result")
            return results[key]
    return inner
