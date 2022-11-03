def cache(func: callable) -> callable:
    # dictionary 'archive' will store arguments given to func (as keys)
    # and func(args) as values
    archive = {}

    def wrapper(*args: tuple) -> callable:
        # if function has already been called with these argument,
        # we seek in archive
        if args in archive.keys():
            print("Getting from cache")
            return archive[args]
        # if new arguments - call the function and add its arguments
        # and return to the archive
        result = func(*args)
        archive[args] = result
        print("Calculating new result")
        return result
    return wrapper
