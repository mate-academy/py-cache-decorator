def cache(func: callable) -> callable:
    results = {}

    def inner(*args) -> callable:
        key = args
        if key in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            res = func(*args)
            results[key] = res
        return results[key]
    return inner
