# Create a Python script that does the following:
# Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.

import sys
import os


def open_and_read(filename):
    print("Current file:", filename)
    current_file = open(filename, "r")
    print(current_file.read())
    current_file.close()


try:
    file_list = set()
    if sys.argv.__len__() < 3:
        raise Exception("There are few arguments.")
    if not os.path.exists(sys.argv[1]):
        raise TypeError("The directory or file does not exist!")
    print("Directory path chosen:", sys.argv[1])
    possible_extensions = ['.pdf', '.py', '.c', '.c++']
    if not sys.argv[2] in possible_extensions:
        raise TypeError("Invalid extension!")
    print("File extension chosen:", sys.argv[2])
    for (root, directories, files) in os.walk(sys.argv[1]):
        file_list.update(set([(os.path.join(root, file)) for file in files]))
    print(file_list)
    file_list = set(map(lambda element: open_and_read(element), filter(lambda file: file.endswith(sys.argv[2]), file_list)))
except ValueError as e:
    print("Invalid mode for opening file.")
except TypeError as e:
    print(e)
except Exception as e:
    print(str(e))
