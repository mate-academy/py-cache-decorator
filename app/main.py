def cache(func):

    stores_results = {}

    def wrapper(*args):

        if args in stores_results:

            print("Getting from cache")

        else:

            stores_results[args] = func(*args)
            print("Calculating new result")

        return stores_results[args]

    return wrapper
