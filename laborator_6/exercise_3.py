# Create a Python script that calculates the total size of all files in a directory provided as a command line
# argument. The script should:
# Use the sys module to read the directory path from the command line. Utilize the os module to iterate through all
# the files in the given directory and its subdirectories. DONE
# Sum up the sizes of all files and display the total size
# in bytes.
# Implement exception handling for cases like the directory not existing, DONE
# permission errors,
# or other file DONE
# access issues.

import sys, os, functools

try:
    total_size = 0
    if sys.argv.__len__() < 2:
        raise Exception("Enter the name of the directory.")
    elif sys.argv.__len__() > 2:
        raise Exception("Too many arguments.")
    if not os.path.exists(sys.argv[1]):
        raise TypeError("The directory or file does not exist!")
    for (root, directories, files) in os.walk(sys.argv[1]):
        print(root, directories, files)
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    print(total_size)
except (Exception, TypeError, OSError) as e:
    print(e)
