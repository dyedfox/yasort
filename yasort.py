#!/usr/bin/env python3
"""
yasort version 1.0.1 - Yet Another Sort Tool
A simple tool for distributing files to folders based on their name prefixes and file extensions.
https://github.com/dyedfox/yasort
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Set, Optional


class Colors:
    """ANSI color codes for terminal output."""
    # Basic colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def is_supported():
        """Check if terminal supports colors."""
        return (
            hasattr(sys.stdout, 'isatty') and sys.stdout.isatty() and
            os.getenv('TERM') != 'dumb' and
            os.name != 'nt' or os.getenv('ANSICON') is not None
        )


def colorize(text: str, color: str = '', bold: bool = False) -> str:
    """Apply color and style to text if terminal supports it."""
    if not Colors.is_supported():
        return text
    
    style = Colors.BOLD if bold else ''
    return f"{style}{color}{text}{Colors.RESET}"


def print_success(message: str):
    """Print success message in green."""
    print(colorize(f"✓ {message}", Colors.GREEN))


def print_error(message: str):
    """Print error message in red."""
    print(colorize(f"✗ {message}", Colors.RED, bold=True))


def print_warning(message: str):
    """Print warning message in yellow."""
    print(colorize(f"⚠ {message}", Colors.YELLOW))


def print_info(message: str):
    """Print info message in blue."""
    print(colorize(f"ℹ {message}", Colors.BLUE))


def print_header(message: str):
    """Print header message in cyan and bold."""
    print(colorize(message, Colors.CYAN, bold=True))


def get_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    Get list of files in directory, optionally filtered by extension.
    
    Args:
        directory: Directory to search in
        extension: File extension to filter by (without dot), or empty string for all files
        
    Returns:
        List of filenames matching the criteria
    """
    try:
        directory_path = Path(directory)
        if not directory_path.exists():
            raise FileNotFoundError(f"Directory '{directory}' does not exist")
        
        all_items = list(directory_path.iterdir())
        files_list = [item.name for item in all_items if item.is_file()]
        
        if extension:
            # Normalize extension (remove leading dot if present)
            ext = extension.lstrip('.')
            files_list = [f for f in files_list if f.lower().endswith(f'.{ext.lower()}')]
        
        return files_list
    except Exception as e:
        print_error(f"Error reading directory: {e}")
        return []


def extract_directory_name(filename: str, delimiter: str, delimiter_position: int, force_string: bool = False) -> Optional[str]:
    """
    Extract directory name from filename based on delimiter or character count.
    
    Args:
        filename: Name of the file
        delimiter: Either a string delimiter or numeric string for character count
        delimiter_position: Position of delimiter from the end (1-based)
        force_string: If True, treat numeric delimiters as string delimiters
        
    Returns:
        Directory name or None if extraction fails
    """
    # Remove file extension first
    name_without_ext = Path(filename).stem
    
    if delimiter.isnumeric() and not force_string:
        # Remove N characters from the end
        char_count = int(delimiter)
        if char_count >= len(name_without_ext):
            return None  # Would result in empty or invalid directory name
        return name_without_ext[:-char_count]
    else:
        # Split by delimiter (treating it as string even if numeric)
        parts = name_without_ext.rsplit(delimiter, delimiter_position)
        if len(parts) <= 1:
            return None  # Delimiter not found enough times
        return parts[0]


def create_directories_and_move_files(files_list: List[str], delimiter: str, 
                                    delimiter_position: int, source_dir: str = ".", force_string: bool = False) -> None:
    """
    Create directories and move files based on naming pattern.
    
    Args:
        files_list: List of files to process
        delimiter: Delimiter or character count for directory extraction
        delimiter_position: Position of delimiter from end
        source_dir: Source directory path
        force_string: If True, treat numeric delimiters as string delimiters
    """
    # Determine directories to create
    directories_to_create = set()
    file_to_dir_mapping = {}
    
    for filename in files_list:
        directory_name = extract_directory_name(filename, delimiter, delimiter_position, force_string)
        if directory_name and directory_name.strip():  # Valid, non-empty directory name
            directories_to_create.add(directory_name)
            file_to_dir_mapping[filename] = directory_name

    if not directories_to_create:
        print_warning('\nNo valid directories can be created from the given files and parameters.')
        print('This might happen if:')
        print('- No files match the delimiter pattern')
        print('- The delimiter would create empty directory names')
        print('- Character count is too large for the filenames')
        return

    # Display directories to be created
    print_header(f'\nDirectories to be created ({len(directories_to_create)} total):')
    print(colorize('Legend: ', Colors.DIM) + 
          colorize('[+] New directory', Colors.GREEN) + ', ' + 
          colorize('[*] Existing directory', Colors.YELLOW) + '\n')
    
    source_path = Path(source_dir)
    for directory_name in sorted(directories_to_create):
        dir_path = source_path / directory_name
        if dir_path.exists():
            print(colorize("[*]", Colors.YELLOW) + f" {directory_name}")
        else:
            print(colorize("[+]", Colors.GREEN) + f" {directory_name}")

    # Get user confirmation
    while True:
        response = input(f'\n{colorize("Do you want to proceed?", Colors.CYAN, bold=True)} (y/n): ').strip().lower()
        if response in ['y', 'yes']:
            break
        elif response in ['n', 'no']:
            print_info('Operation cancelled.')
            return
        else:
            print_warning('Please enter y or n.')

    # Process files
    moved_count = 0
    skipped_count = 0
    error_count = 0
    
    for filename in files_list:
        if filename not in file_to_dir_mapping:
            continue  # Skip files that don't match the pattern
            
        directory_name = file_to_dir_mapping[filename]
        
        try:
            # Create directory
            dir_path = source_path / directory_name
            dir_path.mkdir(exist_ok=True)
            
            # Check if destination file already exists
            source_file = source_path / filename
            dest_file = dir_path / filename
            
            if dest_file.exists():
                while True:
                    response = input(f"\n{colorize('File exists:', Colors.YELLOW)} '{dest_file}' {colorize('Overwrite?', Colors.CYAN)} (y/n/a): ").strip().lower()
                    if response in ['y', 'yes']:
                        source_file.rename(dest_file)
                        print_success(f'Moved (overwritten): {filename} -> {directory_name}/')
                        moved_count += 1
                        break
                    elif response in ['n', 'no']:
                        print_warning(f'Skipped: {filename}')
                        skipped_count += 1
                        break
                    elif response in ['a', 'all']:
                        # TODO: Implement "overwrite all" functionality
                        source_file.rename(dest_file)
                        print_success(f'Moved (overwritten): {filename} -> {directory_name}/')
                        moved_count += 1
                        break
                    else:
                        print_warning('Please enter y (yes), n (no), or a (all).')
            else:
                source_file.rename(dest_file)
                print_success(f'Moved: {filename} -> {directory_name}/')
                moved_count += 1
                
        except Exception as e:
            print_error(f'Error processing {filename}: {e}')
            error_count += 1

    # Summary
    print_header(f'\nOperation Summary:')
    print(f'  Total files processed: {colorize(str(len(file_to_dir_mapping)), Colors.CYAN, bold=True)}')
    print(f'  Files moved: {colorize(str(moved_count), Colors.GREEN, bold=True)}')
    if skipped_count > 0:
        print(f'  Files skipped: {colorize(str(skipped_count), Colors.YELLOW, bold=True)}')
    if error_count > 0:
        print(f'  Errors: {colorize(str(error_count), Colors.RED, bold=True)}')
    
    if error_count == 0:
        print_success('All operations completed successfully!')


def show_interactive_help():
    """Display help information in interactive mode."""
    help_text = f"""
{colorize('YASORT HELP', Colors.CYAN, bold=True)}
{colorize('===========', Colors.CYAN)}

{colorize('WHAT IT DOES:', Colors.GREEN, bold=True)}
yasort organizes files into directories based on patterns in their filenames.

{colorize('HOW IT WORKS:', Colors.GREEN, bold=True)}
1. You specify a delimiter (like '_' or '-') or number of characters
2. yasort extracts the prefix from each filename 
3. Creates directories based on these prefixes
4. Moves files into their corresponding directories

{colorize('EXAMPLES:', Colors.YELLOW, bold=True)}

{colorize('Using a delimiter:', Colors.BLUE)}
- Files: photo_vacation1.jpg, photo_vacation2.jpg, photo_work1.jpg
- Delimiter: '_' (position 1)
- Result: Creates 'photo' directory, moves all files there

{colorize('Using character count:', Colors.BLUE)}
- Files: IMG001.jpg, IMG002.jpg, DOC001.pdf, DOC002.pdf  
- Characters to remove: 3
- Result: Creates 'IMG' and 'DOC' directories

{colorize('Using numbers as string delimiters:', Colors.BLUE)}
- Files: IMG009_1111, IMG009_1, IMG009123
- Delimiter: 9 (with string mode)
- Result: Creates 'IMG00' directory

{colorize('DELIMITER MODES:', Colors.MAGENTA, bold=True)}
- Numeric mode: Remove N characters from end (e.g., '3' removes last 3 chars)
- String mode: Split on delimiter character (e.g., '9' splits on digit '9')
- Use 'string' mode option to force numbers to be treated as delimiters

{colorize('TIPS:', Colors.MAGENTA, bold=True)}
- Test with a small number of files first
- Make backups of important files before running
- Use specific file extensions to limit which files are processed
- The tool shows a preview before making any changes

{colorize('COMMAND LINE OPTIONS:', Colors.CYAN, bold=True)}
  -h, --help              Show this help
  -e, --extension EXT     Process only files with this extension
  -d, --delimiter DELIM   Delimiter string or character count
  -p, --position NUM      Delimiter position from end (default: 1)
  --directory PATH        Directory to process (default: current)
  --string-mode          Treat numeric delimiters as strings
  --version              Show version information

{colorize('Press Enter to continue...', Colors.DIM)}
"""
    print(help_text)
    input()


def main():
    parser = argparse.ArgumentParser(
        description='yasort - Yet Another Sort Tool for organizing files into directories',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  yasort                              # Interactive mode
  yasort -e txt -d _ -p 1             # Sort .txt files using underscore delimiter
  yasort -e jpg -d 3                  # Sort .jpg files by removing last 3 characters
  yasort -e jpg -d 9 --string-mode    # Sort .jpg files using '9' as string delimiter
  yasort --directory /path/to/dir     # Sort files in specific directory
  
COMMON USE CASES:
  Photo organization:    yasort -e jpg -d _ -p 1
  Document sorting:      yasort -e pdf -d 3
  Music file cleanup:    yasort -e mp3 -d " - " -p 1
  Number delimiters:     yasort -e txt -d 9 --string-mode

For detailed help and examples, run in interactive mode or visit:
https://github.com/dyedfox/yasort
        """
    )
    
    parser.add_argument('-e', '--extension', 
                       help='File extension to filter (without dot)')
    parser.add_argument('-d', '--delimiter', 
                       help='Delimiter string or number of characters to remove from end')
    parser.add_argument('-p', '--position', type=int, default=1,
                       help='Delimiter position from end (default: 1)')
    parser.add_argument('--directory', default='.',
                       help='Directory to process (default: current directory)')
    parser.add_argument('--string-mode', action='store_true',
                       help='Treat numeric delimiters as string delimiters instead of character counts')
    parser.add_argument('--version', action='version', version='yasort 1.0.1')
    
    args = parser.parse_args()

    print_header('yasort version 1.0.1 - Yet Another Sort Tool')
    print('A simple tool for distributing files to folders based on their name prefixes.')
    print(colorize('https://github.com/dyedfox/yasort', Colors.BLUE, bold=True))
    print()

    # Interactive mode if no arguments provided
    if not args.delimiter:
        print_info('Interactive mode - Type "help" for detailed information\n')
        
        while True:
            extension = input(f'{colorize("File extension", Colors.CYAN)} (leave blank for all files, "help" for help): ').strip()
            if extension.lower() == 'help':
                show_interactive_help()
                continue
            break
            
        while True:
            delimiter = input(f'{colorize("Delimiter or number of ending characters to remove", Colors.CYAN)} ("help" for help): ')
            if delimiter.lower() == 'help':
                show_interactive_help()
                continue
            elif not delimiter:
                print_error('Delimiter is required.')
                continue
            break
        
        # Ask about string mode for numeric delimiters
        force_string = False
        if delimiter.isnumeric():
            while True:
                mode_input = input(f'{colorize("Numeric delimiter detected. Use as:", Colors.CYAN)} (c)haracter count or (s)tring delimiter? (c/s): ').strip().lower()
                if mode_input in ['c', 'char', 'character']:
                    force_string = False
                    break
                elif mode_input in ['s', 'str', 'string']:
                    force_string = True
                    break
                else:
                    print_warning('Please enter c (character count) or s (string delimiter).')
            
        if not delimiter.isnumeric() or force_string:
            while True:
                position_input = input(f'{colorize("Delimiter position from end", Colors.CYAN)} (default: 1, "help" for help): ').strip()
                if position_input.lower() == 'help':
                    show_interactive_help()
                    continue
                position = int(position_input) if position_input.isnumeric() else 1
                break
        else:
            position = 1
    else:
        extension = args.extension or ''
        delimiter = args.delimiter
        position = args.position
        force_string = args.string_mode

    # Validate inputs
    if not delimiter:
        print_error('Error: Delimiter cannot be empty.')
        sys.exit(1)
        
    if delimiter.isnumeric() and not force_string and int(delimiter) <= 0:
        print_error('Error: Character count must be positive.')
        sys.exit(1)
        
    if position <= 0:
        print_error('Error: Position must be positive.')
        sys.exit(1)

    # Get files and process
    files_list = get_files_by_extension(args.directory, extension)
    
    if not files_list:
        print_warning(f'No files found matching the criteria in "{args.directory}".')
        sys.exit(0)
    
    print_info(f'Found {len(files_list)} file(s) to process.')
    
    # Show mode information
    if delimiter.isnumeric():
        if force_string:
            print_info(f'Using "{delimiter}" as string delimiter (position {position} from end)')
        else:
            print_info(f'Using character count mode: removing last {delimiter} characters')
    else:
        print_info(f'Using "{delimiter}" as string delimiter (position {position} from end)')
    
    create_directories_and_move_files(files_list, delimiter, position, args.directory, force_string)


if __name__ == '__main__':
    main()