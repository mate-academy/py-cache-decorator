def cache(func):
    saved_answers = []

    def inner(*args):
        if len(saved_answers) > 0:
            for item in saved_answers:
                if args in item:
                    print("Getting from cache")
                    return item[1]
        print("Calculating new result")
        answer = func(*args)
        saved_answers.append((args, answer))
        return answer

    return inner
