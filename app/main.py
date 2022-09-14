def cache(func):
    result = {}

    def inner(*args, **kwargs):

        if args not in result:
            res = func(*args, **kwargs)
            result[args] = res
            print("Calculating new result")
        else:
            print("Getting from cache")

        return result[args]

    return inner
