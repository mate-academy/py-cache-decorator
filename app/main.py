def cache(func):
    result = {}

    def inner(*args):
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            new_result = func(*args)
            result.update({args: new_result})
            return new_result
    return inner
