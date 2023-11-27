def merge_files(file_list, result, delim='\n'):
    try:
        file = open(result, 'w')
        for file_name in file_list:
            current_file = open(file_name, 'r')
            file.write(current_file.read())
            file.write(delim)
        return f"Merged files successfully into '{result}'"

    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
