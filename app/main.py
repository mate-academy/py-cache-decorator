def cache(func):
    dict_results = {}

    def inner(*args):
        result = None
        if args in dict_results:
            print("Getting from cache")
            result = dict_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
        dict_results.update({args: result})
        return result
    return inner
