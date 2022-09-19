def cache(func):
    memorized_results = {}

    def wrapper(*args):
        if args not in memorized_results:
            print("Calculating new result")
            memorized_results[args] = func(*args)
        else:
            print("Getting from cache")

        return memorized_results[args]

    return wrapper
