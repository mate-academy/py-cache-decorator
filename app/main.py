def cache(func):
    cached_dict = {}

    def inner(*args):

        if args in cached_dict.keys():
            print("Getting from cache")

            return cached_dict[args]
        else:
            print("Calculating new result")

            result = func(*args)

            cached_dict[args] = result

            return result

    return inner
