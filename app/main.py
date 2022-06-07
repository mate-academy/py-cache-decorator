def cache(func):

    stores_results = {}

    def wrapper(*args):

        if args in stores_results:

            print("Getting from cache")
            return stores_results[args]

        else:

            stores_results[args] = func(*args)
            print("Calculating new result")

            return stores_results[args]

    return wrapper
