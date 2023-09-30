def cache(func: callable) -> callable:
    result = {}

    def inner(*args) -> tuple:
        parameters = args
        if parameters in result.keys():
            print("Getting from cache")
            return result[parameters]
        print("Calculating new result")
        result[parameters] = func(*args)
        return result[parameters]

    return inner
