def cache(func):
    data_cache = dict()

    def inner(*args, **kwargs):
        if args in data_cache:
            print("Getting from cache")
            return data_cache[args]
        else:
            new_result = func(*args, *kwargs)

            data_cache[args] = new_result
            print("Calculating new result")
            return new_result

    return inner
