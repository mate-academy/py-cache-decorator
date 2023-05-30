def cache(func: callable) -> callable:
    results = {}

    def inner(*args) -> callable:
        key = args
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args)
        return results[key]
    return inner
