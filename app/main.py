def cache(func):
    values = []

    def inner(*args, **kwargs):
        nonlocal values

        cached = list(filter(lambda x: x[0] == args, values))
        if cached:
            print("Getting from cache")
            return cached[0][1]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            pre_comp = (args, result, func.__name__)
            values.append(pre_comp)
            return result

    return inner
