# Write a Python script that counts the number of files with each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv).
# Use the os module to list all files in the directory.
# Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# Include error handling for scenarios such as the directory not being found, no read permissions,
# or the directory being empty.

import sys, os

file_extensions = list()
try:
    if not os.path.exists(sys.argv[1]):
        raise TypeError("The directory or file does not exist!")
    files = os.listdir(sys.argv[1])
    split_files = [os.path.splitext(file) for file in files]
    extensions_list = [file[1] for file in split_files]
    print(set(map(lambda element: (element, extensions_list.count(element)), extensions_list)))
except (Exception, TypeError, OSError) as e:
    print(e)
