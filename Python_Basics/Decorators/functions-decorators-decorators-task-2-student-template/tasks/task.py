import logging
import time
from functools import wraps


def log(func):
    # Configure logging with a custom format
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(message)s')

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # Prepare log message
        arg_values = ', '.join(f'{param}={value}' for param, value in zip(func.__code__.co_varnames, args))
        kwarg_values = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        execution_time = round(end_time - start_time, 2)

        log_message = f'{func.__name__}; args: {arg_values}; kwargs: {kwarg_values}'  # Print log message to the console
        print(log_message)

        # Write log message to the file
        logging.info(log_message)

        return result

    return wrapper


if __name__ == "__main__":
    @log
    def foo(a, b, c):
        # print(f"Executing foo with args: a={a}, b={b}, c={c}")
        time.sleep(0.1)  # Simulate some work in the function


    result = foo(1, 2, c=3)

    # Check if log.txt contains the expected log message
    with open('log.txt', 'r') as log_file:
        log_content = log_file.read()

    expected_log_message = 'foo; args: a=1, b=2; kwargs: c=3'
    print(expected_log_message)
    assert expected_log_message in log_content
