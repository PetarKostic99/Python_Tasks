import os


class Cd:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.saved_dir = None

    def __enter__(self):
        # Save the current directory
        self.saved_dir = os.getcwd()

        # Check if the specified directory exists and is a directory
        if not os.path.exists(self.new_dir) or not os.path.isdir(self.new_dir):
            raise ValueError(f"The directory '{self.new_dir}' does not exist or is not a directory.")

        # Change to the new directory
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the original directory
        os.chdir(self.saved_dir)


# Example of usage
try:
    with Cd('/home'):
        # Code inside the 'with' block will run with the current directory changed to '/home'
        print("Current directory inside the 'with' block:", os.getcwd())
except ValueError as e:
    print(e)

# Code outside the 'with' block will have the original current directory restored
print("Current directory outside the 'with' block:", os.getcwd())
