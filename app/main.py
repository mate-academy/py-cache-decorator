def cache(func):
    results = {}

    def inner(*args):
        results
        if args not in results.keys():
            print("Calculating new result")
            result_func = func(*args)
            results[args] = result_func
            return result_func
        else:
            print("Getting from cache")
            return results[args]

    return inner
