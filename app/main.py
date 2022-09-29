def cache(func):
    dt = {}

    def wrapper(*args):
        if not dt.get(args, False) is False:
            print("Getting from cache")
            return dt[args]
        else:
            result = func(*args)
            dt[args] = result
            print("Calculating new result")
            return result

    return wrapper
