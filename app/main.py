
def cache(func: callable) -> any:
    results = {}

    def inner(*args) -> any:
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        else:
            result = func(*args)
            results.update({args: result})
            print("Calculating new result")
            return result
    return inner
