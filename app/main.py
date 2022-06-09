def cache(func):
    cacheDict = {}

    def inner(*args):
        if args not in cacheDict:
            print('Calculating new result')
            res = func(*args)
            cacheDict[args] = res
            return res
        print('Getting from cache')
        return cacheDict[args]
    return inner
