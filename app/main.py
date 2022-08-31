def cache(func):
    storage_result = {}

    def wrapper(*args):

        if storage_result.get(args) is not None:
            print("Getting from cache")
            return storage_result.get(args)

        temp = func(*args)
        storage_result.update({args: temp})
        print("Calculating new result")
        return storage_result.get(args)

    return wrapper
