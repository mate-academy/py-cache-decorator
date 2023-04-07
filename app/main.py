def cache(function):
    result = {}

    def wrapper(*args):
        if args in result.keys():
            print("Getting from cache")

        else:
            result.update({args: function(*args)})
            print("Calculating new result")

        return result[args]
    return wrapper
