import os

def get_files_by_extension(extension):
    current_directory = os.getcwd()
    files_list = os.listdir(current_directory)
    if extension:
        files_list = [f for f in files_list if f.endswith(extension)]
    else:
        files_list = [f for f in files_list if os.path.isfile(os.path.join(current_directory, f))]
    return files_list

def create_directories_from_delimiter(files_list, delimiter):
    for file_name in files_list:
        if delimiter.isdigit():
            directory_name = file_name.rsplit('.', 1)[0][:-int(delimiter)]
        else:
            directory_name = file_name.rsplit('.', 1)[0].rsplit(delimiter, 1)[0]
        if directory_name != file_name:  # Prevents creating directory for files without delimiter
            directory_path = os.path.join(os.getcwd(), directory_name)
            os.makedirs(directory_path, exist_ok=True)
            file_path = os.path.join(os.getcwd(), file_name)
            os.rename(file_path, os.path.join(directory_path, file_name))

def main():
    print('''
    >> fsort version 0.3.1 -  fsort is a simple tool for distributing files to folders based on their name prefixes and file extensions.
    (https://github.com/dyedfox/fsort)

    *Please note: a directory is considered a file with null extension. Be careful while using this option!
    ''')
    extension = input('>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): ')
    delimiter = input('>> Please enter the number of ending characters or delimiter to use for sorting files: ')
    files_list = get_files_by_extension(extension)
    create_directories_from_delimiter(files_list, delimiter)

if __name__ == '__main__':
    main()
