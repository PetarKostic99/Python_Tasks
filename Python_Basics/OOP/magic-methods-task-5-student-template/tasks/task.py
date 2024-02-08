import os
import tempfile
import shutil

class TempDir:
    def __enter__(self):
        self.prev_dir = os.getcwd()

        # Ensure /tmp exists
        if not os.path.exists("/tmp"):
            os.mkdir("/tmp")  # Create /tmp if needed

        # Create the temporary directory within /tmp
        self.temp_dir = tempfile.TemporaryDirectory(dir="/tmp")
        os.chdir(self.temp_dir.name)
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.prev_dir)
        shutil.rmtree(self.temp_dir.name)  # Explicitly use rmtree

with TempDir() as temp_dir:
    print("Current working directory:", os.getcwd())  # Output: The temporary directory path
    with open("test.txt", "w") as f:
        f.write("This file is inside the temporary directory")

# The temporary directory and its contents are removed after exiting the context manager
print("Temporary directory deleted")