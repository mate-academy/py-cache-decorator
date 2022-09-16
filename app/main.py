def cache(func):
    old_results = {}

    def inner(*args):
        if args in old_results:
            print("Getting from cache")
            return old_results[args]
        result = func(*args)
        old_results[args] = result
        print("Calculating new result")
        return result

    return inner
