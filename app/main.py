def cache(func):
    memo = {}

    def wrapper(*args):
        if args not in memo:
            print("Calculating new result")
            memo[args] = func(*args)
        else:
            print("Getting from cache")
        return memo[args]

    return wrapper
