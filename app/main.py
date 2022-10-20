def cache(func):
    dt = {}

    def wrapper(*args) -> int:
        if args in dt:
            print("Getting from cache")
            return dt[args]
        else:
            result = func(*args)
            dt[args] = result
            print("Calculating new result")
            return result

    return wrapper
