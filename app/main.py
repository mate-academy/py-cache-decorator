def cache(func):
    history = {}

    def wrapper(*args, **kwargs):
        if history.get(args):
            print("Getting from cache")
            return history[args]
        else:
            print("Calculating new result")
            result = func(*args)
            history[args] = result
            return result
    return wrapper
