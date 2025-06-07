import os

def get_files_by_extension(extension):
    current_directory = os.getcwd()
    files_list = os.listdir(current_directory)
    if extension:
        files_list = [f for f in files_list if f.endswith(extension)]
    else:
        files_list = [f for f in files_list if os.path.isfile(os.path.join(current_directory, f))]
    return files_list

def create_directories_from_delimiter(files_list, delimiter, delimiter_position):
    directories_to_create = set()
    for file_name in files_list:
        if delimiter.isnumeric():
            directory_name = file_name.rsplit('.', 1)[0][:-int(delimiter)]
        else:
            directory_name = file_name.rsplit('.', 1)[0].rsplit(delimiter, int(delimiter_position))[0]
        if directory_name != file_name:  # Prevents creating directory for files without delimiter. If file doesn't contain delimiter it will be not splitted and a directory can be created by a mistake!
            directories_to_create.add(directory_name)

    if not directories_to_create:
        print('\nNo directories to create. No files to move.')
        return

    print(f'The following directories will be created ({len(directories_to_create)} total, existing ones marked with [*]):\n')
    for directory_name in sorted(directories_to_create):
        if os.path.exists(directory_name):
            exists="[*]"
        else:
            exists="[+]"
        print(f'{exists} {directory_name}')

    user_confirmation = input('\nDo you want to proceed? (Y/n): ').strip().lower() or 'y'
    if user_confirmation != 'y':
        print('\nOperation cancelled.')
        return
    overwrite_count = 0
    skipped_count = 0
    for file_name in files_list:
        if delimiter.isnumeric():
            directory_name = file_name.rsplit('.', 1)[0][:-int(delimiter)]
        else:
            directory_name = file_name.rsplit('.', 1)[0].rsplit(delimiter, int(delimiter_position))[0]
        if directory_name != file_name:
            try:
                directory_path = os.path.join(os.getcwd(), directory_name)
                os.makedirs(directory_path, exist_ok=True)
                file_path = os.path.join(os.getcwd(), file_name)
                if os.path.exists(os.path.join(directory_path, file_name)):
                    user_confirmation = input(f"\nFile '{os.path.join(directory_path, file_name)}' already exists. Do you want to overwrite it? (y/N): ").strip().lower() or 'n'
                    if user_confirmation != 'n':
                        os.rename(file_path, os.path.join(directory_path, file_name))
                        print (f'{file_name} -> {os.path.join(directory_path, file_name)}')
                        overwrite_count += 1
                    else:
                        print (f'{file_name} skipped.')
                        skipped_count += 1
                        pass
                else:
                    os.rename(file_path, os.path.join(directory_path, file_name))
                    print (f'{file_name} -> {os.path.join(directory_path, file_name)}')
            except Exception as e:
                print(f'Error creating directory {directory_name}: {str(e)}')
    print (f'\nOperation completed. {len(files_list)} file(s) total, {skipped_count} file(s) skipped, {overwrite_count} file(s) overwritten.')

def main():
    print('''
yasort version 0.9.0 -  yasort (Yet Another Sort Tool) is a simple tool for distributing files to folders based on their name prefixes and file extensions.
(https://github.com/dyedfox/yasort)

*Please note: a directory is considered a file with null extension. Be careful while using this option!
    ''')
    extension = input('>> Please enter the file extension (you can leave this option blank if you want to sort all files regardless of their extension): ')
    delimiter = input('>> Please enter the number of ending characters or delimiter to use for sorting files: ')
    if delimiter.isnumeric():
        files_list = get_files_by_extension(extension)
        position = 1
    else:
        position = input(">> Please enter the number of delimiter's position from the end (you can leave this option blank to set it to the default value [1]): ")
        if position.isnumeric():
            pass
        else:
            position = 1
        files_list = get_files_by_extension(extension)

    create_directories_from_delimiter(files_list, delimiter, position)

if __name__ == '__main__':
    main()
