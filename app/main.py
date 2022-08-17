def cache(func):
    # Write your code here
    dict_results = {}

    def wrapper(*args):
        nonlocal dict_results
        if args in dict_results:
            print("Getting from cache")
            return dict_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            dict_results.update({args: result})
        return result
    return wrapper
