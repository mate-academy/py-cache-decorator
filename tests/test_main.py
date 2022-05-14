import io

from contextlib import redirect_stdout
from app.main import cache


def test_cache_single_function():
    @cache
    def long_time_func(a, b, c):
        return (a ** b ** c) % (a * c)

    f = io.StringIO()

    with redirect_stdout(f):
        long_time_func(1, 2, 3)
        long_time_func(2, 2, 3)
        long_time_func(1, 2, 3)
        long_time_func(3, 4, 5)
        long_time_func(3, 4, 5)

    out = f.getvalue()

    output = (
        "Calculating new result\n"
        "Calculating new result\n"
        "Getting from cache\n"
        "Calculating new result\n"
        "Getting from cache\n"
    )

    assert (
            out == output
    ), f"""
                output must be:
                {output},

                while calls are:  
                    long_time_func(1, 2, 3)
                    long_time_func(2, 2, 3)
                    long_time_func(1, 2, 3)
                    long_time_func(3, 4, 5)
                    long_time_func(3, 4, 5)
            """


def test_cache_multiple_functions():
    @cache
    def long_time_func(a, b, c):
        return (a ** b ** c) % (a * c)

    @cache
    def long_time_func_2(text_1, text_2):
        return f"{text_1.upper()}, {text_2.lower()}"

    @cache
    def long_time_func_3(n_list, text):
        return f"{[i ** 2 for i in n_list]}, {text}"

    f = io.StringIO()

    with redirect_stdout(f):
        long_time_func(1, 2, 3)
        long_time_func(1, 2, 3)
        long_time_func(1, 2, 3)
        long_time_func_3((10, 20, 30), "wow, numbers!")
        long_time_func(2, 2, 3)
        long_time_func_2("Hello", "world")
        long_time_func(1, 2, 3)
        long_time_func_2("Hello", "Mark")
        long_time_func_2("Hello", "Mark")
        long_time_func_3((10, 20, 30), "wow, numbers!")
        long_time_func_3((10, 20, 30), "egh, numbers...")

    out = f.getvalue()

    output = (
        "Calculating new result\n"
        "Getting from cache\n"
        "Getting from cache\n"
        "Calculating new result\n"
        "Calculating new result\n"
        "Calculating new result\n"
        "Getting from cache\n"
        "Calculating new result\n"
        "Getting from cache\n"
        "Getting from cache\n"
        "Calculating new result\n"
    )

    assert (
        out == output
    ), f"""
            output must be:
            {output},

            while calls are:  
            long_time_func(1, 2, 3)
            long_time_func(1, 2, 3)
            long_time_func(1, 2, 3)
            long_time_func_3((10, 20, 30), 'wow, numbers!')
            long_time_func(2, 2, 3)
            long_time_func_2("Hello", "world")
            long_time_func(1, 2, 3)
            long_time_func_2("Hello", "Mark")
            long_time_func_2("Hello", "Mark")
            long_time_func_3((10, 20, 30), 'wow, numbers!')
            long_time_func_3((10, 20, 30), 'egh, numbers...')
        """


def test_cache_returns_correct_value():
    @cache
    def long_time_func(a, b, c):
        return (a ** b ** c) % (a * c)

    first_value = long_time_func(2, 3, 3)
    second_value = long_time_func(2, 3, 3)

    assert first_value == 2
    assert second_value == 2


def test_cache_depends_on_different_functions():
    @cache
    def subtraction(a, b):
        return a - b

    @cache
    def addiction(a, b):
        return a + b

    f = io.StringIO()

    with redirect_stdout(f):
        subtraction(1, 1)
        addiction(1, 1)
        subtraction(1, 1)
        addiction(1, 1)

    out = f.getvalue()

    output = (
        "Calculating new result\n"
        "Calculating new result\n"
        "Getting from cache\n"
        "Getting from cache\n"
    )

    assert (
            out == output
    ), "Cache decorator should depend on different function"
