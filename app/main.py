def cache(func: callable) -> callable:
    results = {}

    def inner(*args) -> callable:

        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)
        return results[args]
    return inner
