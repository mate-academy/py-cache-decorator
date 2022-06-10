def cache(func):
    stored_data = {}

    def inner(*args):
        if args in stored_data:
            print("Getting from cache")
            result = stored_data[args]
        else:
            result = func(*args)
            stored_data[args] = result
            print("Calculating new result")

        return result

    return inner
