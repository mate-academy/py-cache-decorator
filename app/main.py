def cache(func: callable) -> callable:
    results = {}

    def inner(*args, **kwargs) -> callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            results[key] =  func(*args, **kwargs)
            return  func(*args, **kwargs)

    return inner
