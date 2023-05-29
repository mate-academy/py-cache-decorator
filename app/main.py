def cache(func):
    old_results = {}

    def inner(*args):
        if args in old_results:
            print("Getting from cache")
        else:
            result = func(*args)
            old_results[args] = result
            print("Calculating new result")

        return old_results[args]

    return inner
