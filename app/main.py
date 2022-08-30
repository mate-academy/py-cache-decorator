def cache(func):
    storage = []

    def run(*args):
        nonlocal storage
        for numb, val in enumerate(storage):
            if storage[numb].get(args) is not None:
                print("Getting from cache")
                return storage[numb].get(args)
        out = func(*args)
        storage.append({args: out})
        print("Calculating new result")
        return out
    return run
