def cache(func):
    results_for_cache = {}

    def inc_sort(*args):
        if args in results_for_cache:
            print("Getting from cache")
            return results_for_cache[args]
        else:
            print("Calculating new result")
            results_for_cache[args] = func(*args)
            return results_for_cache[args]

    return inc_sort
