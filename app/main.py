def cache(func):
    cacheDict = {}

    def calculation(*args):
        if args in cacheDict:
            print("Getting from cache")
            return cacheDict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cacheDict[args] = result
            return result
    return calculation
