def cache(func):
    cache_date = []

    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) in cache_date:
            print("Getting from cache")
        else:
            print("Calculating new result")
        cache_date.append(func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrapper
