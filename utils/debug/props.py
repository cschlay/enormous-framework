import logging
import timeit


def duration(function):
    return lambda *args, **kwargs: measure_duration(function, *args, **kwargs)


def measure_duration(function, *args, **kwargs):
    start_time = timeit.default_timer()
    return_value = function(*args, **kwargs)
    end_time = timeit.default_timer()
    logging.debug(end_time - start_time)
    return return_value

