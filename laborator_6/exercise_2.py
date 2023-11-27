# Write a script using the os module that renames all files in a specified directory to have a sequential number
# prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or
# files that can't be renamed.

import os

directory = "G:\Facultate\An3Sem1\python_laboratoare\pregatire_partial\laborator_6\\try"
try:
    if not os.path.exists(directory):
        raise TypeError("The directory does not exist!")
    files = os.listdir(directory)
    files.sort()
    for index, file_name in enumerate(files, start=1):
        file_split = os.path.splitext(file_name)
        os.rename(os.path.join(directory,file_name), os.path.join(directory, file_split[0] + str(index) + file_split[1]))

except Exception as e:
    print(e)
