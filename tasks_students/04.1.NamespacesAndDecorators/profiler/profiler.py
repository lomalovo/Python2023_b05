import datetime


def profiler(func):  # type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """
    calls = 0

    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        return_value = func(*args, **kwargs)
        end = datetime.datetime.now()
        last_time_taken = (end - start).total_seconds()
        return return_value

    return wrapper
