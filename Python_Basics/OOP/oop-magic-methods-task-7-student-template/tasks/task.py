from contextlib import ContextDecorator
from datetime import datetime


class LogFile(ContextDecorator):
    def __init__(self, log_filename):
        self.log_filename = log_filename
        self.log_file = None

    def __enter__(self):
        self.log_file = open(self.log_filename, 'a')
        start_time = datetime.now()
        self.start_timestamp = start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        self.start_time = start_time
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.now()
        run_time = end_time - self.start_time
        run_time_str = "{:.6f}".format(run_time.total_seconds())
        error_message = "None" if exc_type is None else str(exc_value)

        log_line = (
            f"Start: {self.start_timestamp} | "
            f"Run: 0:{run_time_str} | "
            f"An error occurred: {error_message}\n"
        )

        self.log_file.write(log_line)
        self.log_file.close()

        if exc_type is not None:
            # Re-raise the exception
            raise exc_type(exc_value).with_traceback(traceback)


@LogFile('my_trace.log')
def example_function_no_error():
    print("No error occurred")


# Usage with an error
@LogFile('my_trace.log')
def example_function_with_error():
    result = 10 / 0  # Example code that may raise an exception


if __name__ == "__main__":
    try:
        example_function_no_error()
    except Exception as e:
        print(f"Caught an exception: {e}")

    try:
        example_function_with_error()
    except Exception as e:
        print(f"Caught an exception: {e}")
