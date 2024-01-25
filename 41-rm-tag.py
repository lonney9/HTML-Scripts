import os
import sys

# This will strip out an entire line it finds a match on
# For removing custom HTML tags

def remove_keywords_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.strip().startswith('<p class="topics-footer"')]

    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    return filtered_lines != lines

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.lower().endswith('.html'):
                file_path = os.path.join(root, file_name)
                if remove_keywords_lines(file_path):
                    print(f'Removed keywords lines from: {file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        sys.exit(1)

    process_directory(directory_path)
