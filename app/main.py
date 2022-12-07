cache_archive = {}


def cache(func):
    def wrapper(*args, **kwargs):
        if f"{func} {args} {kwargs}" not in cache_archive.keys():
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache_archive[f"{func} {args} {kwargs}"] = res
            return res
        else:
            print("Getting from cache")
            return cache_archive[f"{func} {args} {kwargs}"]

    return wrapper
