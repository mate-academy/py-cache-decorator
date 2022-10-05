def cache(func):
    saved_answers = {}

    def inner(*args):
        if f"{args}" in saved_answers:
            print("Getting from cache")
            return saved_answers[f"{args}"]

        print("Calculating new result")
        answer = func(*args)
        saved_answers[f"{args}"] = answer
        return answer

    return inner
