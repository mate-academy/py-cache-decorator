def cache(func):
    calculation_results = {}

    def wraper(*args):
        if args in calculation_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            calculation_results[args] = func(*args)
        return calculation_results[args]

    return wraper
