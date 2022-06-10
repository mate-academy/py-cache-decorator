def cache(func):
    cached_values_dict = {}

    def inner(*args, **kwargs):

        if args in cached_values_dict:
            print("Getting from cache")
            result = cached_values_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_values_dict[args] = result

        return result

    return inner
