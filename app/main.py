def cache(func: callable) -> any:
    results = {}

    def wrapper(*args) -> any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result
    return wrapper
