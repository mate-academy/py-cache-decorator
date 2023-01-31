
def cache(func: callable) -> any:
    results = {}

    def inner(*args) -> any:
        if args in results:
            print("Getting from cache")
        else:
            results[args] = func(*args)
            print("Calculating new result")
        return results[args]
    return inner
