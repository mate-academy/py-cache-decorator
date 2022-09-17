def cache(func):
    memorized_function_results = {}

    def wrapper(*args):
        if args not in memorized_function_results:
            print("Calculating new result")
            memorized_function_results[args] = func(*args)
        else:
            print("Getting from cache")

        return memorized_function_results[args]

    return wrapper
