def cache(func):
    saved_results = {}

    def wrapper(*args: (int, float), **kwargs: (int, float)) -> dict:
        if args in saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_results[args] = func(*args, **kwargs)

        return saved_results[args]
    return wrapper
