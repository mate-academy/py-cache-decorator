def cache(func):
    results = {}

    def inner(*args):
        if args in results:
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        result = func(*args)
        results[args] = result
        return result
    return inner
